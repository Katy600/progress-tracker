from django.contrib import admin
from .models import StruggleData
# Register your models here.

# admin.site.register(StruggleData)

class StruggleDataAdmin(admin.ModelAdmin):
    list_display = ('time_started', 'title', 'struggle', 'plan', 'frustration_level', 'learning_level', 'code_screen_shot', 'review_learning', 'time_ended', 'struggle_in_progess', 'helpful_link')
    fields = [('title', 'time_started'), 'struggle', 'plan', ('frustration_level', 'learning_level', 'code_screen_shot'), 'review_learning', ('time_ended', 'helpful_link' ), 'struggle_in_progess']

admin.site.register(StruggleData, StruggleDataAdmin)