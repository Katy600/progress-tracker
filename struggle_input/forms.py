from django import forms
import datetime
from django.forms.widgets import NumberInput
from django.forms import ModelForm
from .models import StruggleData

# class StruggleForm(forms.Form):
# 	date = forms.DateField(initial=datetime.date.today)
# 	title = forms.CharField()
# 	struggle = forms.CharField(widget=forms.Textarea, label='Your struggle')
# 	plan = forms.CharField(widget=forms.Textarea, label='Your plan')
# 	time_off_task = forms.IntegerField(help_text='value 1 to 10', widget=NumberInput(attrs={'type':'range',  'step': '1', 'max':'10', 'min':'0', 'value': '5', 'class':'slider', 'id':'id_time_off_task'}))
# 	frustration_level = forms.IntegerField(help_text='value 1 to 10', widget=NumberInput(attrs={'type':'range',  'step': '1', 'max':'10', 'min':'0', 'value': '5', 'class':'slider', 'id':'id_frustration_levels'}))
# 	code_screen_shot = forms.ImageField(required=False, label='Add a screen shot of your code')

class StruggleModelForm(ModelForm):
	frustration_level = forms.IntegerField(widget=NumberInput(attrs={'type':'range',  'step': '1', 'max':'10', 'min':'0', 'value': '5'}))
	time_off_task = forms.IntegerField(widget=NumberInput(attrs={'type':'range',  'step': '1', 'max':'10', 'min':'0', 'value': '5'}))

	class Meta:
		model = StruggleData
		fields = ['title', 'date', 'struggle', 'plan', 'frustration_level', 'time_off_task', 'code_screen_shot']
	
