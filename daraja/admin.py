from django.contrib import admin
from .models import Log

# Register your models here.

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
	list_display = ('date_created', 'title', 'description')
	date_hierachy = 'date_created'
	ordering = ['-date_created']