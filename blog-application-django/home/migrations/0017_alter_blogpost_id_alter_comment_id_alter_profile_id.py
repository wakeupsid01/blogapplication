# Generated by Django 4.1.5 on 2023-02-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_profile_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
