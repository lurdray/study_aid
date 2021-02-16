from django.db import models
from app_user.models import  AppUser
from question.models import Question
from theory.models import Theory

from django.utils import timezone


# Create your models here.


class Cbt(models.Model):
	title = models.CharField(max_length=500)
	cbt_slug = models.CharField(max_length=500, default="no slug")
	cbt_category = models.CharField(max_length=500)
	cbt_level = models.CharField(max_length=500)

	duration = models.CharField(max_length=500)
	
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

	questions = models.ManyToManyField(Question, through="CbtQuestionConnector")
	theorys = models.ManyToManyField(Theory, through="CbtTheoryConnector")


	actual_score = models.IntegerField(default=0)
	total_score = models.IntegerField(default=0)
	percentage = models.IntegerField(default=0)

	corrections = models.TextField()

	status = models.BooleanField(default=False)

	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		#return self.cart_id
		return str(self.title)



class CbtQuestionConnector(models.Model):
	cbt = models.ForeignKey(Cbt, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class CbtTheoryConnector(models.Model):
	cbt = models.ForeignKey(Cbt, on_delete=models.CASCADE)
	theory = models.ForeignKey(Theory, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)







class Result(models.Model):
	#app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	
	app_user_slug = models.CharField(max_length=100, default="none")

	cbt_id = models.CharField(max_length=100, default="none")
	cbt_title = models.CharField(max_length=100, default="none")
	cbt_type = models.CharField(max_length=100, default="none")
	cbt_slug = models.CharField(max_length=100, default="none")

	answers = models.CharField(max_length=100, default="none")
	response_theory = models.TextField(default="none")

	score = models.IntegerField(default=0)
	total = models.IntegerField(default=0)
	percentage = models.IntegerField(default=0)

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		#return self.cart_id
		return str(self.app_user.name)