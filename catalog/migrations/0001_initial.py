# Generated by Django 5.0.6 on 2024-05-08 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование категории",
                        max_length=50,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание",
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование продукта",
                        max_length=50,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание продукта",
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "image_preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото продукта",
                        null=True,
                        upload_to="products/photo",
                        verbose_name="Фото(превью)",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        help_text="Введите цену", max_length=10, verbose_name="Цена"
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        help_text="Введите дату создания", verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        help_text="Введите дату последнего изменения",
                        verbose_name="Дата последнего изменения",
                    ),
                ),
                (
                    "manufactured_at",
                    models.DateField(
                        help_text="Введите дату производства продукта",
                        verbose_name="Дата производства продукта",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите категорию",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["name", "category", "price", "created_at", "updated_at"],
            },
        ),
    ]