# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0002_remove_plate_quantity_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmeal',
            name='properties',
            field=models.CharField(default='', max_length=100, verbose_name='Propiedades'),
        ),
        migrations.AlterField(
            model_name='itemmeal',
            name='amount',
            field=models.IntegerField(default='', verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='itemmeal',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='itemmeal',
            name='value',
            field=models.DecimalField(decimal_places=2, default='', max_digits=9, verbose_name='Valor'),
        ),
    ]