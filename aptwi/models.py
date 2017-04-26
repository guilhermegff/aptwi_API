from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
import uuid

class Genre(models.Model):

	name = models.CharField(max_length=200, help_text="Enter a book genre")

	def __unicode__(self):

		return self.name
