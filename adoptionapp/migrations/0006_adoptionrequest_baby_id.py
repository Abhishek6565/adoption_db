# Generated by Django 2.1.4 on 2020-04-02 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptionapp', '0005_adoptionrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptionrequest',
            name='baby_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
