# Generated by Django 4.0.6 on 2022-07-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blog1'),
        ),
    ]
