# Generated by Django 2.1.15 on 2020-03-15 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vps_price', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vps',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='VPS',
        ),
    ]