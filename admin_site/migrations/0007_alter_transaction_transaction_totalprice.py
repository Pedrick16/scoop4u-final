# Generated by Django 4.1.3 on 2023-03-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0006_alter_pos_pos_reselleramount_alter_pos_pos_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_totalprice',
            field=models.BigIntegerField(default=0, null=True, verbose_name='Total Price'),
        ),
    ]
