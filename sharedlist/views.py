# -*- coding: utf-8 -*-

from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, JsonResponse

from .admin import SharedListForm, SharedListItemForm
from .models import SharedList, SharedListItem

import traceback


@login_required
def sharedlist_detail(request, list_slug=None):

	context = {}

	if request.method == 'POST':

		print("Method is POST!")

		item_form = SharedListItemForm(request.POST)
		if item_form.is_valid():
			item_form.save()
			print("saved item_form")
		else:
			print('item_form is not valid!')


	if list_slug is not None:

		try:
			sharedlist = SharedList.objects.get(slug=list_slug)
			shared_items = sharedlist.get_items()

			context['list'] = sharedlist
			context['items'] = shared_items

		except SharedList.DoesNotExist:
			raise Http404()

		except SharedListItem.DoesNotExist:
			shared_items = []

	try:
		sharedlists = SharedList.objects.all()

	except SharedList.DoesNotExist:
		sharedlists = []

	context['lists'] = sharedlists
	context['list_form'] = SharedListForm()
	context['item_form'] = SharedListItemForm()

	template = loader.get_template('sharedlist/index.html')

	return HttpResponse(template.render(context, request))

@login_required
def sharedlist_add(request, name):

	try:
		sharedlist = SharedList.objects.get(name=name)

		message = 'Failed to add shared list `%s`: A list with that name already exists.' % name
		return JsonResponse({
			'status': 1,
			'message': message,
			'traceback': traceback.format_exc(),
		})

	except SharedList.DoesNotExist:
		pass

	try:
		sharedlist = SharedList(name=name)
		sharedlist.save()

		message = 'Successfully added shared list `%s`.' % name
		return JsonResponse({
			'status': 0,
			'message': message,
		})

	except Exception as err:
		message = err

	return JsonResponse({
		'status': 1,
		'message': message,
		'traceback': format_exc(),
	})

@login_required
def sharedlist_del(request, name):

	try:
		SharedList.objects.get(name=name).delete()

		message = 'Successfully deleted shared list `%s`.' % name
		return JsonResponse({
			'status': 0,
			'message': message,
		})

	except SharedList.DoesNotExist:
		message = 'Failed to delete shared list `%s`: No such list.' % name

	except:
		message = 'Error occured.'

	return JsonResponse({
		'status': 1,
		'message': message,
		'traceback': traceback.format_exc(),
	})

@login_required
def sharedlistitem_add(request, list_slug, item_name):

	try:
		sharedlist = SharedList.objects.get(name=list_name)

	except SharedList.DoesNotExist:
		message = 'No such list `%s`.' % list_name
		return JsonResponse({
			'status': 1,
			'message': message,
			'traceback': traceback.format_exc(),
		})

	return JsonResponse(message)

@login_required
def sharedlistitem_del(request, list_slug, item_name):

	try:
		sharedlist = SharedList.objects.get(name=list_name)

	except SharedList.DoesNotExist:
		message = 'No such list `%s`.' % list_name
		return JsonResponse({
			'status': 1,
			'message': message,
			'traceback': traceback.format_exc(),
		})

	return JsonResponse(message)

@login_required
def sharedlistitem_mark_done(request, list_slug, item_slug, done):

	try:
		sharedlist = SharedList.objects.get(slug=list_slug)

	except SharedList.DoesNotExist:
		message = 'No such list with slug `%s`.' % list_slug
		return JsonResponse({
			'status': 1,
			'message': message,
			'traceback': traceback.format_exc(),
		})

	try:
		new_sharedlist = list_slug != 'all-lists' and sharedlist or None
		item = SharedListItem.objects.get(slug=item_slug, sharedlist=new_sharedlist)

	except SharedList.DoesNotExist:
		message = 'No such item with slug `%s` in list `%s`' % (item_slug, sharedlist.name)
		return JsonResponse({
			'status': 1,
			'message': message,
			'traceback': traceback.format_exc(),
		})

	item.mark_done(done == 1);

	return JsonResponse({
		'status': 0,
		'message': 'Success',
	})
