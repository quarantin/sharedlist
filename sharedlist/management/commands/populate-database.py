# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from sharedlist.models import *

from datetime import timedelta


class Command(BaseCommand):

	def flush_database(self):

		all_models = [
			SharedListItem,
			SharedList,
		]

		self.stdout.write(self.style.MIGRATE_HEADING('Flushing database:'))

		for model in all_models:

			self.stdout.write('  Flushing model `%s`' % model.__name__, ending='')

			try:
				model.objects.all().delete()
				self.stdout.write(self.style.SUCCESS(' OK'))
			except:
				self.stdout.write(self.style.SUCCESS(' MISSING'))

	def handle(self, *args, **options):

		# We want to clear the database before populating it to avoid duplicate entries.
		self.flush_database()

		self.stdout.write(self.style.MIGRATE_HEADING('Populating database:'))

		self.stdout.write('  Populating model `SharedList`', ending='')

		# SharedList: All
		sharedlist_all = SharedList(name='All Lists')
		sharedlist_all.save()

		# SharedList: Shopping
		sharedlist_all = SharedList(name='Shopping')
		sharedlist_all.save()

		self.stdout.write(self.style.SUCCESS(' OK'))
