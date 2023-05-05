# Generated by Django 4.1.2 on 2023-04-22 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0021_alter_return_product_return_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='return_product',
            old_name='product_status',
            new_name='return_status',
        ),
        migrations.AddField(
            model_name='return_product',
            name='reason',
            field=models.TextField(null=True, verbose_name='Reason'),
        ),
        migrations.AddField(
            model_name='return_product',
            name='reseller_name',
            field=models.CharField(max_length=200, null=True, verbose_name='Reseller Name'),
        ),
        migrations.AlterField(
            model_name='return_product',
            name='product_code',
            field=models.CharField(max_length=200, verbose_name='Product Code'),
        ),
    ]
