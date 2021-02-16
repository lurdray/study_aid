from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .forms import UserForm

from app_user.models import AppUser
from study_resource.models import StudyResource

import random
import string


# Create your views here.

def SignInView(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse("main:index"))
			else:
				return HttpResponse("Incorrect Login!")

		else:
			return HttpResponse("Incorrect Login!")
	else:
		context = {}
		return render(request, "main/sign_in.html", context)



def IndexView(request):
	if request.method == "POST":
		pass

		
	else:
		study_resources = sorted(StudyResource.objects.all(), key=lambda x: random.random())[:10]

		context = {"study_resources": study_resources}
		return render(request, "main/index.html", context)






def SignUpView(request):
	if request.method == "POST":

		form = UserForm(request.POST or None, request.FILES or None)


		if request.POST.get("password2") != request.POST.get("password1"):
			return HttpResponse("Error!  -Please make sure both passwords are similar")
			
		else:
			user = form.save()
			user.set_password(request.POST.get("password1"))
			user.save()

			app_user = AppUser.objects.create(user=user)
			app_user.save()

			return HttpResponseRedirect(reverse("main:sign_in"))

	else:
		form = UserForm()
		return render(request, "main/sign_up.html", {"form": form})





def UserLogoutView(request):
	logout(request)
	return HttpResponseRedirect(reverse("main:sign_in"))




def ray_randomiser(length=6):
	landd = string.ascii_letters + string.digits
	return ''.join((random.choice(landd) for i in range(length)))

