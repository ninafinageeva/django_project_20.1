from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Введите описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    objects = None
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание продукта",
    )
    image_preview = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Фото(превью)",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        blank=True,
        null=True,
        related_name='products'
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену"
    )
    created_at = models.DateField(
        verbose_name="Дата создания", help_text="Введите дату создания"
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )
    manufactured_at = models.DateField(
        verbose_name='Дата производства продукта',
        help_text='Введите дату производства продукта'
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "name",
            "category",
            "price",
            "created_at",
            "updated_at",
        ]

    def __str__(self):
        return f"{self.name}, {self.price}"
