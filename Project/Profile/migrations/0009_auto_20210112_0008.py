# Generated by Django 3.1.3 on 2021-01-11 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0008_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]