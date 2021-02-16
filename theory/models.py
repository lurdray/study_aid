from django.db import models
from django.utils import timezone

# Create your models here.
class Theory(models.Model):
	title = models.CharField(max_length=500, default="question")
	question = models.TextField()
	answer = models.TextField(default="None")

	category = models.CharField(max_length=500, default="general")
	level = models.CharField(max_length=500, default="simple")
	
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		#return self.cart_id
		return str(self.title)