# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from meal.models import AuditModel, Plate, Meal, Allergy


class Student(User, AuditModel):
    GENDERS = (
        ('F', 'Feminino'),
        ('M', 'Masculino')
    )
    registration = models.CharField('Matrícula', max_length=255, default='')
    cpf = models.CharField('CPF', max_length=255, default='')
    rg = models.CharField('RG', max_length=255, default='')
    nickname = models.CharField(
        'Apelido', max_length=255, null=True, blank=True)
    gender = models.CharField(
        'Gênero', max_length=1, choices=GENDERS, default='')
    father_name = models.CharField('Nome do Pai', max_length=255, default='')
    father_occupation = models.CharField(
        'Profissão do Pai', max_length=255, default='')
    mother_name = models.CharField('Nome da Mãe', max_length=255, default='')
    mother_occupation = models.CharField(
        'Profissão da Mãe', max_length=255, default='')
    phone = models.CharField('Telefone', max_length=15, default='')
    birth = models.DateField('Data de Nascimento')
    postal_code = models.CharField('CEP', max_length=9, default='')
    city = models.CharField('Cidade', max_length=255, default='')
    address = models.CharField('Endereço', max_length=255, default='')
    address_number = models.CharField('Número', max_length=255, default='')
    district = models.CharField('Bairro', max_length=255, default='')
    reference = models.CharField(
        'Referência', max_length=255, null=True, blank=True)
    photo = models.ImageField(
        'Foto', upload_to='cadastro-aluno/', null=True, blank=True)
    allergy = models.ManyToManyField(
        Allergy,
        verbose_name='Alergias',
        related_name='allergy_student',
        blank=True)

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('student:student_list')

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'


class Check(AuditModel):
    student = models.ForeignKey(
        Student, verbose_name='Aluno', related_name='student_check')
    plate = models.ForeignKey(
        Plate, verbose_name='Prato', related_name='plate_check')
    meal = models.ForeignKey(
        Meal, verbose_name='Refeição', related_name='meal_check')

    def __str__(self):
        return '%s - %s' % (self.plate.name, self.student.get_full_name())

    def get_absolute_url(self):
        return reverse('student:check_list')
