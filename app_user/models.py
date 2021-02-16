from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class AppUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=500)
	account_type = models.CharField(max_length=500)
	status = models.BooleanField(default=False)

	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.username