from unicodedata import category
from django import forms
from .choices import *


class JobRegisterForm(forms.Form):
    title = forms.CharField(label='Title', max_length=20, required=True)
    description = forms.CharField(label='Description', widget=forms.Textarea, max_length=3000, required=True)
    minimum_salary = forms.IntegerField()
    maximum_salary = forms.IntegerField()
    category = forms.ChoiceField(label='Category', choices=CATEGORY_CHOICES, required=True)
    image = forms.ImageField()


class FormEditUser(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=20, required=False)
    last_name = forms.CharField(label='Last Name', max_length=20, required=False)
    image = forms.ImageField(label='Image', required=False)
    experience = forms.CharField(label='Experience', widget=forms.Textarea, max_length=400, required=False)
