# Generated by Django 2.1.4 on 2020-03-24 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptionapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
