# Generated by Django 4.1.1 on 2023-06-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0010_alter_product_short_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='short_name',
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]