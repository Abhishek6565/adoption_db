# Generated by Django 2.1.4 on 2020-05-15 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptionapp', '0010_parentsinfo_aadhar_copy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationinfo',
            name='Charity_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]