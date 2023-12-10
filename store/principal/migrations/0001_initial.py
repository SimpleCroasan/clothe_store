# Generated by Django 4.2.7 on 2023-12-09 23:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Descripcion', models.CharField(max_length=1000)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('Unidades_disponibles', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]