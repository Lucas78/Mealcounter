# -*- coding: utf-8 -*-

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class EditAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Valido o email para ser obrigatório
        if email == '':
            raise forms.ValidationError('O endereço de email é obrigatório.')

        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Este endereço de email já está em uso. Por favor, use um ' +
                'email diferente.')
        return email


class PasswordResetForm(PasswordResetForm):

    def clean_email(self):
        user = get_user_model()._default_manager.filter(
            email__iexact=self.cleaned_data.get('email'), is_active=True)
        if not user.exists():
            raise forms.ValidationError(
                'Lamentamos, mas não reconhecemos esse endereço de e-mail.')
        return self.cleaned_data.get('email')
