# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-14 08:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(choices=[('LA', '지각'), ('EA', '조퇴'), ('AB', '결석'), ('OU', '외출')], max_length=2)),
                ('event_date', models.DateTimeField(auto_now_add=True)),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StudyClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studyclass', models.CharField(choices=[('202', '202반'), ('203', '203반')], max_length=3)),
                ('unit', models.PositiveIntegerField()),
                ('limit', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='check.StudyClass'),
        ),
        migrations.AddField(
            model_name='student',
            name='stu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
