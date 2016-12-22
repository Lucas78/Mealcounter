# -*- coding: utf-8 -*-

from django import forms
from .models import *
from dal import autocomplete
from django.db.models import Sum
from django.db.models.functions import Coalesc

class StudentForm(forms.ModelForm)

	class Student:
		model = Student
		elds = ('__all__')
		widgets = {'adc_student': autocomplete.ModelSelect2Multiple(url='adc_student:adc_student_autocomplete')}
