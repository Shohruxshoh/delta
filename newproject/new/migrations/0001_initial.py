# Generated by Django 3.1.5 on 2021-01-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
