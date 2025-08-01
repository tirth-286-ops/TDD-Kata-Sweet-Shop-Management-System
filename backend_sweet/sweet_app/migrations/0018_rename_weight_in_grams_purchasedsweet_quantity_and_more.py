# Generated by Django 5.0 on 2025-07-27 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_app', '0017_remove_purchasedsweet_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasedsweet',
            old_name='weight_in_grams',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='purchasedsweet',
            name='buyer_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='purchasedsweet',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='sweet',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
