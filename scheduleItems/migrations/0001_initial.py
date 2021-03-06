# Generated by Django 2.2.11 on 2020-05-21 17:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('learnGroups', '0003_auto_20200521_2013'),
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('duration', models.TimeField(default=django.utils.timezone.now)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='learnGroup', to='learnGroups.LearnGroup')),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson', to='lessons.Lesson')),
            ],
        ),
    ]
