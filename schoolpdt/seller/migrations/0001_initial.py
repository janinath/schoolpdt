# Generated by Django 5.0 on 2023-12-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.TextField(max_length=50)),
                ('c_image', models.ImageField(blank=True, upload_to='photos/category')),
            ],
        ),
    ]
