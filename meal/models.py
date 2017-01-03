# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class AuditModel(models.Model):
    created_on = models.DateTimeField('Criado em', auto_now_add=True)
    updated_on = models.DateTimeField('Autalizado em', auto_now=True)

    class Meta:
        abstract = True


class Allergy(AuditModel):
    name = models.CharField('Descrição', max_length=100, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meal:allergy_list')

    class Meta:
        verbose_name = 'Alergia'
        verbose_name_plural = 'Alergias'


class ItemMeal(AuditModel):
    name = models.CharField('Nome', max_length=100, default='')
    properties = models.TextField(
        'Propriedades', max_length=100, null=True, blank=True)
    allergy = models.ManyToManyField(
        Allergy,
        verbose_name='Alergias',
        related_name='allergy_item',
        blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meal:item_meal_list')

    class Meta:
        verbose_name = 'Item Refeição'
        verbose_name_plural = 'Itens da Refeição'
        ordering = ['-id']


class Plate(AuditModel):
    name = models.CharField('Descrição', max_length=100)
    item_meal = models.ManyToManyField(
        ItemMeal, verbose_name='Itens da Refeição', related_name='item_plate')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meal:plate_list')

    class Meta:
        verbose_name = 'Prato Feito'
        verbose_name_plural = 'Pratos Feitos'
        ordering = ['-id']


class Meal(AuditModel):
    date = models.DateField('Data')
    estimate = models.IntegerField('Estimativa')
    start_time = models.TimeField('Início')
    end_time = models.TimeField('Término')
    status = models.BooleanField('Ativo')
    plate = models.ManyToManyField(
        Plate, verbose_name='Prato', related_name='plate_meal')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meal:meal_list')

    class Meta:
        verbose_name = 'Refeição'
        verbose_name_plural = 'Refeições'
        ordering = ['-id']
