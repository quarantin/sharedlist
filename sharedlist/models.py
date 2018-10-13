from django.db import models
from django.utils.text import slugify

import traceback


class SharedList(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, default='')

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		new_slug = slugify(self.name)
		if self.slug is None or self.slug != new_slug:
			self.slug = new_slug

		super(SharedList, self).save(*args, **kwargs)

	def add_item(self, item_name):
		item = SharedListItem(name=item_name, sharedlist=self)
		item.save()

	def del_item(self, item_name):
		try:
			item = SharedListItem.objects.get(name=item_name, sharedlist=self)
			item.delete()

		except SharedListItem.DoesNotExist:
			return 1, 'Error: %s' % traceback.format_exc()

		return 0, 'Success'

	def get_items(self):

		if self.slug == 'all-lists':
			items = SharedListItem.objects.all()
		else:
			items = SharedListItem.objects.filter(sharedlist=self)

		return items.order_by('done', 'sharedlist', 'name')

class SharedListItem(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, default='')
	sharedlist = models.ForeignKey(SharedList, on_delete=models.SET_NULL, blank=True, null=True)
	done = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	due_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return '%s / %s' % (self.sharedlist, self.name)

	def save(self, *args, **kwargs):
		new_slug = slugify(self.name)
		if self.slug is None or self.slug != new_slug:
			self.slug = new_slug

		super(SharedListItem, self).save(*args, **kwargs)

	def mark_done(self, done):
		self.done = done
		self.save(update_fields=['done'])

class UserPreference(models.Model):

	user = models.User()
	confirm_mark_done = models.BooleanField(default=True)
	confirm_mark_undone = models.BooleanField(default=True)
