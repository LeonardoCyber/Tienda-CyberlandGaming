# Generated by Django 4.0.6 on 2022-07-15 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='contenido',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='Servicios'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]