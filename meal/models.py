# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class AuditModel(models.Model):
    created_on = models.DateTimeField('Criado em', auto_now_add=True)
    updated_on = models.DateTimeField('Autalizado em', auto_now=True)

    class Meta:
        abstract = True


class ItemMeal(AuditModel):
    name = models.CharField('Nome', max_length=100, default='')
    amount = models.IntegerField('Quantidade', default='')
    value = models.DecimalField(
        'Valor', max_digits=9, decimal_places=2, default='')
    properties = models.CharField('Propriedades', max_length=100, default='')

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
    item_meal = models.ManyToManyField(ItemMeal)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meal:plate_list')

    class Meta:
        verbose_name = 'Prato Feito'
        verbose_name_plural = 'Pratos Feitos'
        ordering = ['-id']


class Meal(AuditModel):
    meal_date = models.DateField('Data da Refeição')
    name = models.CharField('Descrição', max_length=100)
    estimate = models.IntegerField('Estimativa')
    start_time = models.TimeField('Inicio da Refeição')
    end_time = models.TimeField('Fim da Refeição')
    status = models.BooleanField('Ativo')
    plate = models.ForeignKey(
        Plate, verbose_name='Prato', related_name='meals')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meal:meal_list')

    class Meta:
        verbose_name = 'Refeição'
        verbose_name_plural = 'Refeições'
        ordering = ['-id']
