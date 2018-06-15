from django.db import models
from datetime import date
from django.forms.widgets import NumberInput
from django.core.validators import *
from django.core.files.base import ContentFile
from django.core.files import File
import os
import glob

class StruggleData(models.Model):
	title = models.CharField(max_length=40)
	date = models.DateField(default=date.today)
	struggle = models.TextField()
	plan = models.TextField(verbose_name ='plan of action')
	frustration_level = models.IntegerField(verbose_name="frustration level (Rate 0 to 10)")
	time_off_task = models.IntegerField(verbose_name="time off task (Rate 0 to 10)")
	code_screen_shot = models.FileField(blank=True, null=True)

	def __str__(self):
		return 'Title: %s, Date: %s, Struggle: %s, Plan: %s, Frustration Level: %s, Time Off Task: %s' % (self.title, self.date, self.struggle, self.plan, self.frustration_level, self.time_off_task)

	class Meta:
		ordering = ["-date", "title"]
