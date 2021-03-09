from django import forms
from django.forms import ModelForm
from . models import *


class ToDoForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add New Task...'}))
	class Meta:
		model = ToDo
		fields = '__all__'