# Generated by Django 5.1 on 2025-01-22 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_womenyoga_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='kidsautumnwinter',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]