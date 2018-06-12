from django.db import models
from datetime import date
from django.forms.widgets import NumberInput
from django.core.validators import *

# Create your models here.

class StruggleData(models.Model):
	title = models.CharField(max_length=40)
	date = models.DateField(default=date.today)
	struggle = models.TextField(help_text="enter your struggles here")
	plan = models.TextField(help_text="enter your plan of action here", verbose_name ='plan of action')
	frustration_level = models.IntegerField()
	time_off_task = models.IntegerField(default=5, help_text='value 1 to 10', validators=[MaxValueValidator(10),
            MinValueValidator(1)])
	code_screen_shot = models.ImageField(blank=True, verbose_name ='add a screen shot of your code')


	def __str__(self):
		return u'Title: %s, Date: %s, Struggle: %s, Plan: %s, Frustration Level: %s, Time Off Task: %s' % (self.title, self.date, self.struggle, self.plan, self.frustration_level, self.time_off_task)


	def get_absolute_url(self):
	    """
	    Returns the url to access a particular instance of the model.
	    """
	    return reverse('model-detail-view', args=[str(self.id)])

	class Meta:
		ordering = ["title", "date"]