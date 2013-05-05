from django.db import models


class Paste(models.Model):
	text = models.TextField()
