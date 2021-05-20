# Generated by Django 3.2.3 on 2021-05-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_faculty_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='image',
        ),
        migrations.AddField(
            model_name='faculty',
            name='image',
            field=models.ImageField(default='image/default/profile.jpg', upload_to='image/image/'),
        ),
    ]
