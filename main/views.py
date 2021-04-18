from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserForm

from app_user.models import AppUser, ContactForm, ContactMessage
from study_resource.models import *

import random
import string


# Create your views here.

#def LandingPageView(request):

	#return render(request, "main/landing_page.html")


def SignInView(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				messages.success(request, "Welcome onboard ")
				return HttpResponseRedirect(reverse("main:index"))
			else:
				messages.warning(request, "Incorrect Login")
				return HttpResponseRedirect(reverse("main:sign_in"))

		else:
			messages.warning(request, "Incorrect Login")
			return HttpResponseRedirect(reverse("main:sign_in"))
	else:
		context = {}
		return render(request, "main/sign_in.html", context)


def SearchView(request):
	if request.method == "POST":
		query = request.POST.get("query")

		resources = StudyResource.objects.filter(title__icontains=query)

		context = {"resources": resources}
		return render(request, "main/result.html", context)


	else:
		context = {}
		return render(request, "main/search.html", context)


def IndexView(request):
	if request.user.is_active == True:
		if request.method == "POST":
			pass

			
		else:
			study_resources = sorted(StudyResource.objects.all(), key=lambda x: random.random())[:10]

			ebooks = sorted(Ebook.objects.all(), key=lambda x: random.random())[:10]
			videos = sorted(Video.objects.all(), key=lambda x: random.random())[:10]
			contents = sorted(Content.objects.all(), key=lambda x: random.random())[:10]
			links = sorted(Link.objects.order_by("-pub_date"), key=lambda x: random.random())[:10]
			forums = sorted(StudyResource.objects.all(), key=lambda x: random.random())[:10]


			context = {"study_resources": study_resources, "links": links, "forums": forums,
			"videos": videos, "ebooks": ebooks, "contents": contents,}
			return render(request, "main/index.html", context)


	else:
		return HttpResponseRedirect(reverse("main:sign_up"))



def ProfileView(request):
	if request.user.is_active == True:

		app_user = AppUser.objects.get(user__pk=request.user.id)

		if request.method == "POST":
			username = request.POST.get("username")
			full_name = request.POST.get("full_name")
			phone = request.POST.get("phone")
			email = request.POST.get("email")
			bio = request.POST.get("bio")
			gender = request.POST.get("gender")
			location = request.POST.get("location")


			if username != "":
				app_user.user.username = username
			if full_name != "":
				app_user.full_name = full_name
			if phone != "":
				app_user.phone = phone
			if email != "":
				app_user.email = email
			if bio != "":
				app_user.bio = bio
			if bio != "":
				app_user.gender = gender
			if bio != "":
				app_user.location = location


			try:
				file = request.FILES["image"]
				app_user.image = file

			except:
				pass


			app_user.save()
			messages.success(request, "Profile Updated successfully")
			return HttpResponseRedirect(reverse("main:profile"))

		else:

			ebooks = Ebook.objects.filter(contributor=app_user.user.username)
			videos = Video.objects.filter(contributor=app_user.user.username)
			contents = Content.objects.filter(contributor=app_user.user.username)
			links = Link.objects.filter(contributor=app_user.user.username)
			images = Image.objects.filter(contributor=app_user.user.username)

			forums = Chat.objects.filter(contributor__pk=app_user.id)

			resources = StudyResource.objects.filter(creator__pk=app_user.id)

			context = {"app_user": app_user, "ebooks": ebooks, "videos": videos,
			"contents": contents, "links": links, "images": images, "forums": forums, "resources": resources}
			return render(request, "main/profile.html", context)


	else:
		return HttpResponseRedirect(reverse("main:sign_up"))






def SignUpView(request):
	if request.method == "POST":

		form = UserForm(request.POST or None, request.FILES or None)


		if request.POST.get("password2") != request.POST.get("password1"):
			messages.warning(request, "Make Sure both passwords match")
			return HttpResponseRedirect(reverse("main:sign_up"))
			
		else:
			try:
				AppUser.objects.get(user__username=request.POST.get("username"))
				messages.warning(request, "Username already exist, try another one!")
				return HttpResponseRedirect(reverse("main:sign_up"))

			except:
				user = form.save()
				user.set_password(request.POST.get("password1"))
				user.save()

				app_user = AppUser.objects.create(user=user)
				app_user.save()
				messages.warning(request, "One final step")
				return HttpResponseRedirect(reverse("main:sign_in"))

	else:
		form = UserForm()
		return render(request, "main/sign_up.html", {"form": form})





def UserLogoutView(request):
	logout(request)
	messages.success(request, "Logged Out successfully")
	return HttpResponseRedirect(reverse("main:landing_page"))





def AboutView(request):
	if request.method == "POST":
		pass

	else:
		context = {}
		return render(request, "main/about.html", context)


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			data = ContactMessage()
			data.name = form.cleaned_data['name']
			data.email = form.cleaned_data['email']
			data.phone = form.cleaned_data['phone']
			data.subject = form.cleaned_data['subject']
			data.message = form.cleaned_data['message']
			data.ip = request.META.get('REMOTE_ADDR')
			data.save()
			messages.success(request, "Your message has been delivered")
			return HttpResponseRedirect(reverse("main:contact"))

	form = ContactForm
	
	context = {'form':form, }
	return render(request,  "main/contact.html", context)

def all_contacts(request):
	contacts = ContactMessage.objects.all()

	context = {'contacts':contacts}
	return render(request, "main/all_contacts.html", context)



def ray_randomiser(length=6):
	landd = string.ascii_letters + string.digits
	return ''.join((random.choice(landd) for i in range(length)))



