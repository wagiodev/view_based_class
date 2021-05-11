from django import forms
from django.forms import ValidationError
from datetime import date


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(max_length=30, required=True, label="username",
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                    }
                                ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))
