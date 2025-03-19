# Generated by Django 5.1.4 on 2025-03-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('alternative_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=250)),
                ('dob', models.DateField(blank=True, null=True)),
                ('Reasons', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
                ('next_meet', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
