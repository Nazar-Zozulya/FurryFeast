# Generated by Django 4.1.1 on 2023-06-10 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Catalog', '0012_product_promotion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=32)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catalog.product')),
            ],
        ),
    ]
