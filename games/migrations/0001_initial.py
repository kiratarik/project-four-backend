# Generated by Django 3.2.7 on 2021-09-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=1000)),
                ('rules', models.TextField(max_length=5000)),
            ],
        ),
    ]
