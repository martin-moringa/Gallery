# Generated by Django 3.0.8 on 2020-08-03 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0011_auto_20200803_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='description',
            new_name='descriptio',
        ),
        migrations.AlterField(
            model_name='photos',
            name='tag',
            field=models.ManyToManyField(to='gallery.Tag'),
        ),
    ]
