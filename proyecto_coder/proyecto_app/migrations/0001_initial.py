# Generated by Django 4.0.6 on 2022-08-16 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('author', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Celphone',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('id', models.FloatField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('brand', models.CharField(max_length=40)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=50)),
                ('id', models.FloatField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=40)),
            ],
        ),
    ]
