from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from theory.models import Theory

import random
import string

# Create your views here.


def ShareTheoryView(request):
	if request.method == "POST":
		question = request.POST.get("question")
		answer = request.POST.get("answer")

		level = request.POST.get("level")
		category = request.POST.get("category")

		theory = Theory.objects.create(question=question, answer=answer, level=level, category=category)
		theory.save()

		return HttpResponseRedirect(reverse("main:index"))
		
	else:

		context = {}
		return render(request, "theory/share.html", context)



def EditTheoryView(request):
	pass



def AllTheoryView(request, category, level):
	theorys = sorted(Theory.objects.filter(category=category, level=level), key=lambda x: random.random())

	if request.method == "POST":
		pass

		
	else:

		context = {"theorys": theorys}
		return render(request, "theory/all_theory.html", context)


	