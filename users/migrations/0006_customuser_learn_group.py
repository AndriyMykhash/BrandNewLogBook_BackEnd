# Generated by Django 2.2.11 on 2020-05-20 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200519_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='learn_group',
            field=models.CharField(default='-', max_length=5),
        ),
    ]