from django.contrib import admin

from .models import Thought


@admin.register(Thought)
class ThoughtAdmin(admin.ModelAdmin):
	pass