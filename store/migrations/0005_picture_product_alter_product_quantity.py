# Generated by Django 4.0.4 on 2022-05-07 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_picture_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='store.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='quantity'),
        ),
    ]
