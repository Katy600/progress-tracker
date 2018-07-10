from django.db import models
from datetime import date, timedelta, datetime
from django.forms.widgets import NumberInput
from django.core.validators import *
from django.core.files.base import ContentFile
from django.core.files import File
import os
import glob

class StruggleData(models.Model):
	title = models.CharField(max_length=40)
	time_started = models.DateTimeField(default=datetime.now)
	time_ended = models.DateTimeField(default=datetime.now, blank=True, null=True)
	struggle = models.TextField()
	plan = models.TextField(verbose_name ='plan of action')
	frustration_level = models.IntegerField(verbose_name="frustration level (Rate 0 to 10)")
	learning_level = models.IntegerField(verbose_name="learning level (Rate 0 to 10)", blank=True, null=True)
	code_screen_shot = models.FileField(blank=True, null=True)
	code_screen_shot_update = models.FileField(blank=True, null=True)
	review_learning = models.TextField(blank=True, null=True)
	struggle_in_progess = models.BooleanField(default=False)
	helpful_link = models.URLField(blank=True, null=True)
	
	def __str__(self):
		return 'Title: %s, Date: %s, Struggle: %s, Plan: %s, Frustration Level: %s, Learning Level: %s, Review Learning: %s, Time spent on struggle: %s, Struggle in progress: %s, Helpful link: %s' % (self.title, self.time_started, self.struggle, self.plan, self.frustration_level, self.learning_level, self.review_learning, self.time_ended, self.struggle_in_progess, self.helpful_link)

	class Meta:
		ordering = ["-time_started", "title"]
