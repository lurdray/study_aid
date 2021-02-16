from django.db import models

from django.utils import timezone

# Create your models here.

class Content(models.Model):
	title = models.CharField(max_length=500)
	content = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)


class Ebook(models.Model):
	title = models.CharField(max_length=500)
	ebook = models.FileField(upload_to='resource/ebooks/', blank=True)
	pub_date = models.DateTimeField(default=timezone.now)


class Video(models.Model):
	title = models.CharField(max_length=500)
	video = models.FileField(upload_to='resource/videos/', blank=True)
	pub_date = models.DateTimeField(default=timezone.now)


class Audio(models.Model):
	title = models.CharField(max_length=500)
	audio = models.FileField(upload_to='resource/audios/', blank=True)
	pub_date = models.DateTimeField(default=timezone.now)



class Image(models.Model):
	title = models.CharField(max_length=500)
	image = models.FileField(upload_to='resource/images/', blank=True)
	pub_date = models.DateTimeField(default=timezone.now)



class Link(models.Model):
	title = models.CharField(max_length=500)
	link = models.CharField(max_length=500)
	pub_date = models.DateTimeField(default=timezone.now)



class StudyResource(models.Model):
	cover_image = models.FileField(upload_to='cover_image/images/', blank=True)
	title = models.CharField(max_length=500)
	description = models.CharField(max_length=500)

	study_level = models.CharField(max_length=500)
	study_category = models.CharField(max_length=500)

	contents = models.ManyToManyField(Content, through="StudyResourceContentConnector")
	ebooks = models.ManyToManyField(Ebook, through="StudyResourceEbookConnector")
	videos = models.ManyToManyField(Video, through="StudyResourceVideoConnector")
	audios = models.ManyToManyField(Audio, through="StudyResourceAudioConnector")
	images = models.ManyToManyField(Image, through="StudyResourceImageConnector")
	links = models.ManyToManyField(Link, through="StudyResourceLinkConnector")

	pub_date = models.DateTimeField(default=timezone.now)


	def __str__(self):
	 	return self.title



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









