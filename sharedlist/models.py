from django.db import models


class SharedList(models.Model):
	name = models.CharField(max_length=255)

class SharedListItem(models.Model):
	name = models.CharField(max_length=255)
	shared_list = models.ForeignKey(SharedList, on_delete=models.SET_NULL, null=True)
