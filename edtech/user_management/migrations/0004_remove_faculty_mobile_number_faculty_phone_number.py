# Generated by Django 4.1 on 2022-09-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_remove_faculty_email_remove_faculty_faculty_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='mobile_number',
        ),
        migrations.AddField(
            model_name='faculty',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
