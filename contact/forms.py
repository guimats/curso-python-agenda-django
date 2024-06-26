from django import forms  # type: ignore
from django.core.exceptions import ValidationError  # type: ignore
from django.contrib.auth.forms import UserCreationForm  # type: ignore
from . import models


class ContactForm(forms.ModelForm):

    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'classe-a classe-b',
    #             'placeholder': 'Escreva aqui'
    #         }
    #     ),
    #     label='Primeiro nome',
    #     help_text='Texto para ajudar o usuário',
    # )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    # self.fields['first_name'].widget.attrs.update({
    #     'class': 'classe-a classe-b',
    #     'placeholder': 'Escreva aqui'
    # })

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category', 'picture'
        )

        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui'
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = (ValidationError(
                'Primeiro nome não pode ser igual ao sobrenome')
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

            return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )
        return first_name


class RegisterForm(UserCreationForm):
    ...
