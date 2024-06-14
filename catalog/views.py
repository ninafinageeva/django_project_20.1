from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version
from catalog.services import get_products_from_cache


class ProductListView(ListView):
    """Класс для отображения списка товаров"""
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(name=product)
            active_versions = versions.filter(version_now=True)
            if active_versions:
                product.active_version = active_versions.last().version_name
            else:
                product.active_version = 'Стартовая'

        context_data['object_list'] = products
        return context_data

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Класс для создания нового товара"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:homepage')

    def form_valid(self, form):
        """Переопределяем метод для привязки к пользователю"""
        if form.is_valid:
            new_object = form.save(commit=False)
            new_object.owner = self.request.user
            new_object.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для обновления товара"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:homepage')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        Versionformset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = Versionformset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = Versionformset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_edit_description") and user.has_perm(
                "catalog.can_edit_publication_sign") and user.has_perm("catalog.can_edit_category"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Класс для удаления товара"""
    model = Product
    success_url = reverse_lazy('catalog:homepage')
