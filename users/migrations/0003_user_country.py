# Generated by Django 5.0.6 on 2024-06-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="country",
            field=models.CharField(
                default="Не указанно",
                help_text="Введите вашу страну",
                max_length=50,
                verbose_name="Страна",
            ),
        ),
    ]
