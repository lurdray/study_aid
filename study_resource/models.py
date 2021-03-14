from django.db import models
from django.utils.text import slugify
from django.utils import timezone

from app_user.models import AppUser

# Create your models here.

class Chat(models.Model):
	title = models.CharField(max_length=500)
	chat = models.TextField()
	contributor = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class Content(models.Model):
	title = models.CharField(max_length=500)
	content = models.TextField()
	contributor = models.CharField(max_length=500, default="Anonymous")
	pub_date = models.DateTimeField(default=timezone.now)


class Ebook(models.Model):
	title = models.CharField(max_length=500)
	ebook = models.FileField(upload_to='resource/ebooks/', blank=True)
	contributor = models.CharField(max_length=500, default="Anonymous")
	pub_date = models.DateTimeField(default=timezone.now)


class Video(models.Model):
	title = models.CharField(max_length=500)
	video = models.FileField(upload_to='resource/videos/', blank=True)
	contributor = models.CharField(max_length=500, default="Anonymous")
	pub_date = models.DateTimeField(default=timezone.now)


class Audio(models.Model):
	title = models.CharField(max_length=500)
	audio = models.FileField(upload_to='resource/audios/', blank=True)
	contributor = models.CharField(max_length=500, default="Anonymous")
	pub_date = models.DateTimeField(default=timezone.now)



class Image(models.Model):
	title = models.CharField(max_length=500)
	image = models.FileField(upload_to='resource/images/', blank=True)
	contributor = models.CharField(max_length=500, default="Anonymous")
	pub_date = models.DateTimeField(default=timezone.now)



class Link(models.Model):
	title = models.CharField(max_length=500)
	link = models.CharField(max_length=500)
	contributor = models.CharField(max_length=500, default="Anonymous")
	pub_date = models.DateTimeField(default=timezone.now)



class StudyResource(models.Model):
	cover_image = models.FileField(upload_to='cover_image/images/', blank=True)
	title = models.CharField(max_length=500)
	description = models.CharField(max_length=500)

	study_level = models.CharField(max_length=500)
	study_category = models.CharField(max_length=500)

	chats = models.ManyToManyField(Chat, through="StudyResourceChatConnector")
	contents = models.ManyToManyField(Content, through="StudyResourceContentConnector")
	ebooks = models.ManyToManyField(Ebook, through="StudyResourceEbookConnector")
	videos = models.ManyToManyField(Video, through="StudyResourceVideoConnector")
	audios = models.ManyToManyField(Audio, through="StudyResourceAudioConnector")
	images = models.ManyToManyField(Image, through="StudyResourceImageConnector")
	links = models.ManyToManyField(Link, through="StudyResourceLinkConnector")

	creator = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	slug = models.SlugField(unique=True, default="rayslug")
	pub_date = models.DateTimeField(default=timezone.now)

	
	def save(self, *args, **kwargs):
		var = self.title +"-" + str(self.pub_date)
		self.slug = slugify(var)
		super().save(*args, **kwargs)
		
	def get_absolute_url(self):
		return "/resource/%s/"%self.slug
		
	def __str__(self):
		return self.title



class StudyResourceChatConnector(models.Model):
	study_resource = models.ForeignKey(StudyResource, on_delete=models.CASCADE)
	chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class StudyResourceContentConnector(models.Model):
	study_resource = models.ForeignKey(StudyResource, on_delete=models.CASCADE)
	content = models.ForeignKey(Content, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class StudyResourceEbookConnector(models.Model):
	study_resource = models.ForeignKey(StudyResource, on_delete=models.CASCADE)
	ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class StudyResourceVideoConnector(models.Model):
	study_resource = models.ForeignKey(StudyResource, on_delete=models.CASCADE)
	video = models.ForeignKey(Video, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class StudyResourceAudioConnector(models.Model):
	study_resource = models.ForeignKey(StudyResource, on_delete=models.CASCADE)
	audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class StudyResourceImageConnector(models.Model):
	study_resource = models.ForeignKey(StudyResource, on_delete=models.CASCADE)
	image = models.ForeignKey(Image, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class StudyResourceLinkConnector(models.Model):
	study_resource = models.ForeignKey(StudyResource, on_delete=models.CASCADE)
	link = models.ForeignKey(Link, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)









