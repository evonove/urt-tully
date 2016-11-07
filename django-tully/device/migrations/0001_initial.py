# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-04 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RPM', models.IntegerField()),
                ('INJ1', models.IntegerField()),
                ('INJ2', models.IntegerField()),
                ('IGN1', models.IntegerField()),
                ('IGN2', models.IntegerField()),
                ('WTEMP', models.IntegerField()),
                ('AIRTEMP', models.IntegerField()),
                ('AIRP', models.IntegerField()),
                ('OILT', models.IntegerField()),
                ('TPS', models.IntegerField()),
                ('LAMBDA', models.IntegerField()),
                ('LAMBDA_TRG', models.IntegerField()),
                ('SPEED_FL', models.IntegerField()),
                ('SPEED_FR', models.IntegerField()),
                ('SPEED_RL', models.IntegerField()),
                ('SPEED_RR', models.IntegerField()),
                ('VBATT', models.IntegerField()),
                ('AUX', models.IntegerField()),
                ('DET', models.IntegerField()),
                ('FCMP', models.IntegerField()),
                ('ECU_ERROR', models.IntegerField()),
                ('FPGA_ERROR', models.IntegerField()),
                ('STATUS', models.IntegerField()),
                ('DELTA', models.IntegerField()),
                ('DWELL', models.IntegerField()),
                ('MAP_TC_SEL', models.IntegerField()),
                ('SLPF_FL', models.IntegerField()),
                ('SLPF_FR', models.IntegerField()),
                ('SLPF_RL', models.IntegerField()),
                ('SLPF_RR', models.IntegerField()),
                ('CUTOFF', models.IntegerField()),
                ('TIME', models.IntegerField()),
                ('AUX_DATA1', models.IntegerField()),
                ('AUX_DATA2', models.IntegerField()),
                ('AUX_DATA3', models.IntegerField()),
                ('AUX_DATA4', models.IntegerField()),
                ('AUX_DATA5', models.IntegerField()),
                ('AUX_DATA6', models.IntegerField()),
                ('AUX_DATA7', models.IntegerField()),
                ('AUX_DATA8', models.IntegerField()),
                ('AUX_DATA9', models.IntegerField()),
                ('AUX_DATA10', models.IntegerField()),
                ('AUX_DATA11', models.IntegerField()),
                ('AUX_DATA12', models.IntegerField()),
                ('AUX_DATA13', models.IntegerField()),
                ('AUX_DATA14', models.IntegerField()),
                ('AUX_DATA15', models.IntegerField()),
                ('AUX_DATA16', models.IntegerField()),
                ('AUX_DATA17', models.IntegerField()),
                ('AUX_DATA18', models.IntegerField()),
                ('AUX_DATA19', models.IntegerField()),
                ('AUX_DATA20', models.IntegerField()),
                ('AUX_DATA21', models.IntegerField()),
                ('AUX_DATA22', models.IntegerField()),
                ('AUX_DATA23', models.IntegerField()),
                ('AUX_DATA24', models.IntegerField()),
                ('AUX_DATA25', models.IntegerField()),
                ('AUX_DATA26', models.IntegerField()),
                ('AUX_DATA27', models.IntegerField()),
                ('AUX_DATA28', models.IntegerField()),
                ('AUX_DATA29', models.IntegerField()),
                ('AUX_DATA30', models.IntegerField()),
                ('AUX_DATA31', models.IntegerField()),
                ('AUX_DATA32', models.IntegerField()),
            ],
        ),
    ]
