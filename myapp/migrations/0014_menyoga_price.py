# Generated by Django 5.1 on 2025-01-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_menrunning_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='menyoga',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]