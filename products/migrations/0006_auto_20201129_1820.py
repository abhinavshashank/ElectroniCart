# Generated by Django 3.1.1 on 2020-11-29 12:50

from django.db import migrations, models
import products.storages


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='media',
            field=models.FileField(default=None, storage=products.storages.ProtectedStorage(), upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default=None, max_length=220),
        ),
    ]
