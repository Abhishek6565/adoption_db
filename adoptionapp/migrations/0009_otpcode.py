# Generated by Django 2.1.4 on 2020-04-17 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptionapp', '0008_auto_20200403_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtpCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp_code', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]