# Generated by Django 3.2.3 on 2021-05-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_alter_faculty_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
