# Generated by Django 4.2.4 on 2023-11-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0009_alter_bookborrowhistory_fine'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookborrowhistory',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]