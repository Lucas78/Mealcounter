# -*- coding: utf-8 -*-
from django.db import models
from meal.models import AuditModel


class Student(AuditModel):
    SEXO_C = (('F', 'Feminino'), ('M', 'Masculino'),)
    num_matricula = models.CharField(
        "Numero da Matricula", max_length=255, null=True)
    cpf = models.CharField(max_length=255, null=True)
    rg = models.CharField(max_length=255, null=True)
    apelido = models.CharField(max_length=255, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_C, blank=True)
    nome_pai = models.CharField(
        max_length=255, verbose_name="Nome do Pai", null=True)
    prof_pai = models.CharField(
        max_length=255, verbose_name="Profissão", null=True)
    nome_mae = models.CharField(
        max_length=255, verbose_name="Nome da Mãe", null=True, blank=True)
    prof_mae = models.CharField(
        max_length=255, verbose_name="Profissão", null=True, blank=True)
    telefone = models.CharField(
        max_length=20,
        verbose_name="Telefone para contato",
        null=True,
        blank=True)
    datanascimento = models.DateField(
        verbose_name="Data de Nascimento", blank=True)
    endereco = models.CharField(
        max_length=255, verbose_name="Endereço", null=True, blank=True)
    num = models.CharField(
        max_length=255, verbose_name="Numero", null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    datacadastro = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='cadastro-aluno/', null=True)
    texto = models.TextField(verbose_name="Descrição", null=True)

    class Meta:
        ordering = ['created_on']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
