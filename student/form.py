# -*- coding: utf-8 -*-

from django import forms
from .models import Student
from dal import autocomplete


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {'adc_student': autocomplete.ModelSelect2Multiple(
            url='adc_student:adc_student_autocomplete')}
