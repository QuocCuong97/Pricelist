# Generated by Django 2.1 on 2020-03-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vps',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
