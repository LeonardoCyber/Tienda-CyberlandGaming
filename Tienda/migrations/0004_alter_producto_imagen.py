# Generated by Django 4.0.6 on 2022-07-21 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Imagen',
            field=models.ImageField(default=1, upload_to='Tienda'),
            preserve_default=False,
        ),
    ]
