from django import forms
import datetime
from django.forms.widgets import NumberInput
from django.forms import ModelForm
from .models import StruggleData
from datetime import date


class StruggleModelForm(ModelForm):
	frustration_level = forms.IntegerField(label='Frustration level (rate 0 to 10)', widget=NumberInput(attrs={'type':'range',  'step': '1', 'max':'10', 'min':'0', 'value': '5'}))
	time_off_task = forms.IntegerField(label='Time off task (rate 0 to 10)', widget=NumberInput(attrs={'type':'range',  'step': '1', 'max':'10', 'min':'0', 'value': '5'}))
	struggle = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your struggle here...'}))
	code_screen_shot = forms.FileField(label='Select a file',)
	class Meta:
		model = StruggleData
		fields = ['title', 'date', 'struggle', 'plan', 'frustration_level', 'time_off_task', 'code_screen_shot']
		ordering = ['-priority', 'date'] 