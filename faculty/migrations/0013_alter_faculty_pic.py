# Generated by Django 3.2.3 on 2021-05-17 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0012_faculty_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='pic',
            field=models.ImageField(default='default/profile.jpg', upload_to='image/'),
        ),
    ]
