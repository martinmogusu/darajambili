from django.db import models

# Create your models here.

class Log(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return self.title
