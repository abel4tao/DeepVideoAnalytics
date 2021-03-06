# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-29 10:04
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0017_auto_20180520_0602'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrameRegionRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_frame_index', models.IntegerField(default=-1)),
                ('target_frame_index', models.IntegerField(default=-1)),
                ('source_segment_index', models.IntegerField(null=True)),
                ('target_segment_index', models.IntegerField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Label')),
                ('source_frame', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_frame', to='dvaapp.Frame')),
                ('source_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_region', to='dvaapp.Region')),
                ('target_frame', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_target', to='dvaapp.Frame')),
                ('target_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_region', to='dvaapp.Region')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video')),
            ],
        ),
    ]
