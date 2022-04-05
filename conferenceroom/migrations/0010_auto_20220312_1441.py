# Generated by Django 3.2.9 on 2022-03-12 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferenceroom', '0009_auto_20220307_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='dateofuse',
            field=models.DateField(max_length=50),
        ),
        migrations.AlterField(
            model_name='room',
            name='timeuse',
            field=models.TimeField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='contactNum',
            field=models.CharField(blank=True, default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='emailadd',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='fname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='lname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]