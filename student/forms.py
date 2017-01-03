# -*- coding: utf-8 -*-

from django import forms
from dal import autocomplete
from .models import Student, Check


class StudentForm(forms.ModelForm):
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.EmailField(label='E-mail')

    class Meta:
        model = Student
        fields = [
            'registration', 'first_name', 'last_name', 'nickname', 'email',
            'cpf', 'rg', 'gender', 'father_name', 'father_occupation',
            'mother_name', 'mother_occupation', 'phone', 'birth',
            'postal_code', 'city', 'address', 'address_number', 'district',
            'reference', 'photo', 'allergy'
        ]
        widgets = {'allergy': autocomplete.ModelSelect2Multiple(
            url='meal:allergy_autocomplete')}


class CheckForm(forms.ModelForm):

    class Meta:
        model = Check
        fields = '__all__'
