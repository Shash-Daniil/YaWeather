from django.db import models
import datetime

class Author(models.Model):
	"""пост"""
	id = models.CharField("id поста", max_length = 30, primary_key = True)
	name = models.CharField("Имя поста", max_length = 50)
	text = models.TextField("Текст поста")
	date = models.DateTimeField(default=datetime.datetime.now())