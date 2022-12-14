# Generated by Django 4.1 on 2022-10-02 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_date', models.DateField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_management.faculty')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_management.university')),
            ],
        ),
    ]
