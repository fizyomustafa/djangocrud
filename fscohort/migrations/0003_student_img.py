# Generated by Django 4.0.4 on 2022-05-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0002_alter_student_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Resim Yükle'),
        ),
    ]