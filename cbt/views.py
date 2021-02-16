from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from question.models import Question
from theory.models import Theory
from cbt.models import Cbt, CbtQuestionConnector, CbtTheoryConnector
from app_user.models import AppUser
from main.views import ray_randomiser

import random
import string

# Create your views here.


def SetupCbtView(request):
	if request.user.is_active == True:
		if request.method == "POST":

		 	question_count = int(request.POST.get("question_count"))
		 	theory_count = int(request.POST.get("theory_count"))

		 	category = request.POST.get("category")
		 	level = request.POST.get("level")
		 	duration = request.POST.get("duration")

		 	app_user = AppUser.objects.get(user__pk=request.user.id)
		 	cbt_slug = ray_randomiser()

		 	title = "cbt(%s) for %s: %s" % (category, app_user, cbt_slug)

		 	cbt = Cbt.objects.create(app_user=app_user, title=title, cbt_slug=cbt_slug, cbt_level=level, cbt_category=category, duration=duration)
		 	cbt.save()

		 	questions = sorted(Question.objects.filter(category=category, level=level), key=lambda x: random.random())[:question_count]
		 	theorys = sorted(Theory.objects.filter(category=category, level=level), key=lambda x: random.random())[:theory_count]

		 	for item in questions:
		 		cbt_question =  CbtQuestionConnector(cbt=cbt, question=item)
		 		cbt_question.save()

		 	for item in theorys:
		 		cbt_theory =  CbtTheoryConnector(cbt=cbt, theory=item)
		 		cbt_theory.save()


		 	return HttpResponseRedirect(reverse("cbt:take_cbt", args=(cbt.id,)))

		else:
			context = {}
			return render(request, 'cbt/setup_cbt.html', context)


	else:
		return HttpResponse("Not Authorised!, Please contact NigTech(www.NigTech.net)")		





def TakeCbtView(request, cbt_id):
	cbt = Cbt.objects.get(id=cbt_id)

	questions = cbt.questions.all()
	counts = cbt.questions.count()
	count_list = []


	for i in range(counts):
		count_list.append(i+1)

	cbt_questions = zip(questions, count_list)

	if request.method == "POST":
		score = 0
		percentage = 0
		actual_score = 0
		real_score = 0

		answers = []
		answer_list = []
		for item, count in cbt_questions:
			val = "selected_answer_" + str(count)
			if request.POST.get(val):
				answers.append(request.POST.get(val))
			else:
				answers.append("x_x")

		for item in answers:
			answer_list.append(item.split("_")[1])


		for item, item2 in zip(cbt.questions.all(), answer_list):
			if item.real_answer == item2:
				actual_score += 1

		percentage = (actual_score/counts)*100

		#percentage, answer_list, actual_score, total_score, 

		cbt.actual_score = actual_score
		cbt.total_score = count
		cbt.percentage = percentage
		cbt.save()

		return HttpResponseRedirect(reverse("cbt:complete_cbt", args=(cbt.id,)))


	else:
		context = {"cbt": cbt, "cbt_questions": cbt_questions}#, "time_exam_link": time_exam_link, "time_student_id": time_student_id}#, "time_result_id": time_result_id}
		return render(request, "cbt/take_cbt.html", context)




def CompleteCbtView(request, cbt_id):
	cbt = Cbt.objects.get(id=cbt_id)

	theorys = cbt.theorys.all()
	counts = cbt.theorys.count()
	count_list = []

	for i in range(counts):
		count_list.append(i+1)

	cbt_theorys = zip(theorys, count_list)

	context = {"cbt": cbt, "cbt_theorys": cbt_theorys}
	return render(request, "cbt/complete_cbt.html", context)









