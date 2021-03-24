from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm, Textarea, TextInput, Select


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

class ContactMessage(models.Model):
	STATUS = (
		('New', 'New'),
		('Read', 'Read'),
		('Closed', 'Closed'),
	)
	name = models.CharField(blank=True, max_length=20)
	email = models.CharField(blank=True, max_length=50)
	subject = models.CharField(blank=True, max_length=50)
	message = models.TextField(blank=True, max_length=1255)
	status = models.CharField(max_length=15, choices=STATUS, default='New')
	ip = models.CharField(blank=True, max_length=20)
	phone = models.CharField(blank=True, max_length=100)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class ContactForm(ModelForm):
	class Meta:
		model = ContactMessage
		fields = ['name', 'email', 'subject', 'message', 'phone']
		widgets = {
			'name'		: TextInput(attrs={'class': 'input','placeholder':'Name & Surname'}),
			'phone'		: TextInput(attrs={'class': 'input','placeholder':'Phone Number'}),
			'subject'	: TextInput(attrs={'class': 'input','placeholder':'Subject'}),
			'email'		: TextInput(attrs={'class': 'input','placeholder':'Email Address'}),
			'message'	: Textarea(attrs={'class': 'input', 'placeholder':'Your Message', 'rows':'5'}),

		}