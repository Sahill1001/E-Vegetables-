# Generated by Django 3.0.5 on 2023-02-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.CharField(choices=[('grams', (('250', '250'), ('500', '500'))), ('kg', (('1', '1'),))], max_length=50, null=True),
        ),
    ]
