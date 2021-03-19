from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class AppUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.FileField(upload_to='resource/profile_images/', blank=True, default="resource/default.jpeg")
	full_name = models.CharField(max_length=500, default="none")
	phone = models.CharField(max_length=500, default="none")
	email = models.CharField(max_length=500, default="none")
	gender = models.CharField(max_length=500, default="none")
	location = models.CharField(max_length=500, default="none")
	bio = models.TextField(default="none")
	account_type = models.CharField(max_length=500, default="none")
	status = models.BooleanField(default=False)

	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.username