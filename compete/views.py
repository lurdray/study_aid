from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from compete.models import *
from question.models import *
from app_user.models import AppUser
from main.views import ray_randomiser

import random
import string

# Create your views here.


def SetupCompeteView(request):
	if request.method == "POST":
		question_count = int(request.POST.get("question_count"))
		level = request.POST.get("level")
		category = request.POST.get("category")
		duration = request.POST.get("duration")
		audience = request.POST.get("audience")

		app_user = AppUser.objects.get(user__pk=request.user.id)
		compete_slug = ray_randomiser()

		title = "compete(%s) for %s: %s" % (category, app_user, compete_slug)

		compete = Compete.objects.create(app_user=app_user, title=title, compete_slug=compete_slug, compete_level=level, compete_category=category, duration=duration, audience=audience)
		compete.save()

		questions = sorted(Question.objects.filter(category=category, level=level), key=lambda x: random.random())[:question_count]

		for item in questions:
			compete_question =  CompeteQuestionConnector(compete=compete, question=item)
			compete_question.save()

		return HttpResponseRedirect(reverse("compete:compete"))


	else:
		context = {}
		return render(request, "compete/setup.html", context)


	


def ResultView(request):
	if request.method == "POST":
		pass


	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)
		competes = Compete.objects.filter(app_user__pk=app_user.id)


		context = {"competes": competes}
		return render(request, "compete/result.html", context)



def JoinCompeteView(request):
	compete_slug = request.POST.get("compete_slug")
	if request.method == "POST":
		#compete_slug = request.POST.get("compete_slug")
		return HttpResponse(compete_slug)


	else:
		return HttpResponse(compete_slug)




def ResultDetailView(request, id):
	compete = Compete.objects.get(id=id)
	compete_id = compete.id

	app_user = AppUser.objects.get(user__pk=request.user.id)

	questions = compete.questions.all()
	counts = compete.questions.count()
	count_list = []


	for i in range(counts):
		count_list.append(i+1)

	compete_questions = zip(questions, count_list)


	if request.method == "POST":
		score = 0
		percentage = 0
		actual_score = 0
		real_score = 0

		answers = []
		answer_list = []
		for item, count in compete_questions:
			val = "selected_answer_" + str(count)
			if request.POST.get(val):
				answers.append(request.POST.get(val))
			else:
				answers.append("x_x")

		for item in answers:
			answer_list.append(item.split("_")[1])


		for item, item2 in zip(compete.questions.all(), answer_list):
			if item.real_answer == item2:
				actual_score += 1

		percentage = (actual_score/counts)*100

		result = Result.objects.create(app_user=app_user, compete_id=compete_id, 
		 score=actual_score, total=count, percentage=percentage) 
		result.save()

		return HttpResponse("Complete!!!")



	else:
		

		try:
			results = Result.objects.filter(compete_id=compete_id)
		except:
			results = None


		if results:
			context = {"results": results}
			return render(request, "compete/result_detail.html", context)


		else:
			context = {"compete": compete, "compete_questions": compete_questions}#, "time_exam_link": time_exam_link, "time_student_id": time_student_id}#, "time_result_id": time_result_id}
			return render(request, "compete/take_compete.html", context)


			

