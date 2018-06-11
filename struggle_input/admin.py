from django.contrib import admin
from .models import StruggleData
# Register your models here.

# admin.site.register(StruggleData)

class StruggleDataAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'struggle', 'plan', 'frustration_level', 'time_off_task', 'code_screen_shot')
    fields = [('title', 'date'), 'struggle', 'plan', ('frustration_level', 'time_off_task', 'code_screen_shot')]

admin.site.register(StruggleData, StruggleDataAdmin)