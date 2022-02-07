from django.core.exceptions import ValidationError

from authentification import forms
from . import validators


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir une lettre', code='password_no_letters')

    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule.'


class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not any(character.is_digit() for character in password):
            raise ValidationError(
                'Le mot de passe doit contenir une chiffre', code='password_no_numbers')

    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins un chiffre.'


# Validator pour un autre champ de formulaire
class PostCodeValidator:
    post_code = forms.CharField(max_length=10, validators=[validators.PostCodeValidator])