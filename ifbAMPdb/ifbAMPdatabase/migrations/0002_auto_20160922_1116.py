# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifbAMPdatabase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peptide',
            name='alpha_beta',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='peptide',
            name='alpha_beta_hdl',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='peptide',
            name='alpha_hdl',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='peptide',
            name='beta_hdl',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='peptide',
            name='hdl',
            field=models.BooleanField(),
        ),
    ]
