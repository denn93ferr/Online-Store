# Generated by Django 4.0.3 on 2022-05-06 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='store.product'),
        ),
        migrations.AlterModelTable(
            name='order',
            table='orders',
        ),
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
    ]