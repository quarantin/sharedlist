from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *


class SharedListForm(forms.ModelForm):

	class Meta:
		model = SharedList

		fields = [
			'name',
		]

		labels = {
			'name': _('Name'),
		}

	def __init__(self, *args, **kwargs):
		super(SharedListForm, self).__init__(*args, **kwargs)
		for field_name in self.fields:
			self.fields[field_name].widget.attrs['class'] = 'form-control'

class SharedListAdmin(admin.ModelAdmin):

	form = SharedListForm

	list_display = [
		'name',
		'slug',
	]

	fieldsets = (

		('Shared List', { 'fields': (
			'name',
			'slug',
		)}),
	)

	def get_readonly_fields(self, request, obj=None):
		return self.readonly_fields + ( 'slug', )

class SharedListItemForm(forms.ModelForm):

	class Meta:
		model = SharedListItem

		fields = [
			'name',
			'sharedlist',
			'due_date',
		]

		labels = {
			'name': _('Name'),
			'sharedlist': _('List'),
			'due_date': _('Due Date'),
		}

	def __init__(self, *args, **kwargs):
		super(SharedListItemForm, self).__init__(*args, **kwargs)
		for field_name in self.fields:
			self.fields[field_name].widget.attrs['class'] = 'form-control'

class SharedListItemAdmin(admin.ModelAdmin):

	form = SharedListItemForm

	list_display = [
		'name',
		'slug',
		'done',
		'sharedlist',
	]

	fieldsets = (

		('Shared List Item', { 'fields': (
			'name',
			'slug',
			'done',
			'sharedlist',
		)}),
	)

	def get_readonly_fields(self, request, obj=None):
		return self.readonly_fields + ( 'slug', )

admin.site.register(SharedList, SharedListAdmin)
admin.site.register(SharedListItem, SharedListItemAdmin)
