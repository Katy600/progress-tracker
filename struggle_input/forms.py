from django import forms
import datetime

class StruggleForm(forms.Form):
	date = forms.DateField(initial=datetime.date.today)
	title = forms.CharField()
	struggle = forms.CharField(widget=forms.Textarea, label='Your struggle')
	plan = forms.CharField(widget=forms.Textarea, label='Your plan')
	frustration_level = forms.IntegerField()
	time_off_task = forms.IntegerField()
	code_screen_shot = forms.ImageField(required=False, label='Add a screen shot of your code')