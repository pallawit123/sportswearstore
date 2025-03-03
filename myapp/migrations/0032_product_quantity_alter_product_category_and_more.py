# Generated by Django 5.1 on 2025-01-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_rename_phone_contact_contact_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_image_path/default.jpg', upload_to='products/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
