from django import forms
import datetime
from django.forms.widgets import NumberInput
from django.forms import ModelForm
from .models import StruggleData
from datetime import date, timedelta


class StruggleModelForm(ModelForm):
    frustration_level = forms.IntegerField(label='Frustration level (rate 0 to 10)', widget=NumberInput(attrs={'type':'range',  'step': '1', 'max':'10', 'min':'0', 'value': '5'}))
    learning_level = forms.IntegerField(required=False, label='Learning level (rate 0 to 10)', widget=NumberInput(attrs={'type':'range',  'step': '1', 'max':'10', 'min':'0', 'value': '5'}))
    struggle = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your struggle here...'}))
    # struggle_in_progess = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = StruggleData
        fields = ['title', 'time_started', 'time_ended', 'struggle', 'plan', 'frustration_level', 'learning_level', 'code_screen_shot', 'review_learning','struggle_in_progess', 'helpful_link']
        ordering = ['-priority', 'time_started'] 
