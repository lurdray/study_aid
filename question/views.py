from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from question.models import Question

# Create your views here.


def ShareQuestionView(request):
	if request.method == "POST":

		q1 = request.POST.get("q1")
		category = request.POST.get("category")
		level = request.POST.get("level")

		if q1 != "":
			q1_a = request.POST.get("q1_a")
			q1_b = request.POST.get("q1_b")
			q1_c = request.POST.get("q1_c")
			q1_d = request.POST.get("q1_d")
			real_answer_1 = request.POST.get("real_answer_1")

			question1 = Question.objects.create(title=q1, answer_a=q1_a, answer_b=q1_b, answer_c=q1_c, answer_d=q1_d, real_answer=real_answer_1, category=category, level=level)
			question1.save()
	
		return HttpResponseRedirect(reverse("main:index"))

		

	else:
		context = {}
		return render(request, "question/share.html", context)




def EditQuestionView(request):
	if request.method == "POST":
		pass
		

	else:
		context = {}
		return render(request, "question/share.html", context)


	