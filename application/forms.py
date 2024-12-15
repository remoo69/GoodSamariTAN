from django import forms
from .models import NGOApplication
from django.core.exceptions import ValidationError

class NGOApplicationForm(forms.ModelForm):
    class Meta:
        model = NGOApplication
        fields = ['ein', 'name', 'address', 'contact_number', 'email', 'password', 'form_990']

    def clean_ein(self):
        ein = self.cleaned_data.get('ein')
        if NGOApplication.objects.filter(ein=ein).exists():
            raise ValidationError("This EIN is already registered.")
        return ein

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if NGOApplication.objects.filter(name=name).exists():
            raise ValidationError("This organization name is already taken.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if NGOApplication.objects.filter(email=email).exists():
            raise ValidationError("This email address is already registered.")
        return email
