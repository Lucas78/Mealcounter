# -*- coding: utf-8 -*-

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class EditAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class PasswordResetForm(PasswordResetForm):

    def clean_email(self):
        user = get_user_model()._default_manager.filter(
            email__iexact=self.cleaned_data.get('email'), is_active=True)
        if not user.exists():
            raise forms.ValidationError(
                'Lamentamos, mas não reconhecemos esse endereço de e-mail.')
        return self.cleaned_data.get('email')
