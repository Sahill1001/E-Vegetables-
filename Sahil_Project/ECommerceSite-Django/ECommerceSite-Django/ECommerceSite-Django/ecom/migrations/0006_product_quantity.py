# Generated by Django 3.0.5 on 2023-02-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_feedback_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.CharField(choices=[('Gram0', '250'), ('Gram1', '500'), ('Kg', '1')], max_length=50, null=True),
        ),
    ]
