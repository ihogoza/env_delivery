# Generated by Django 4.0 on 2021-12-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0002_alter_medicine_m_expirydate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='in_stock',
            field=models.IntegerField(default=0),
        ),
    ]
