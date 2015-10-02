# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issue', models.CharField(max_length=100)),
                ('severity', models.SmallIntegerField()),
                ('probability', models.SmallIntegerField()),
                ('instruction', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('planname', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('state', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('regtime', models.TimeField()),
                ('level', models.SmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='owner',
            field=models.ForeignKey(to='onlinebandit.user'),
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(to='onlinebandit.plan'),
        ),
    ]
