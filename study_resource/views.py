from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from main.views import ray_randomiser

from study_resource.models import *
from app_user.models import AppUser

import random
import string

# Create your views here.


def SetupShareView(request):
	if request.user.is_active == True:
		if request.method == "POST":

		 	category = request.POST.get("category")
		 	level = request.POST.get("level")

		 	study_resources = sorted(StudyResource.objects.filter(study_category=category, study_level=level), key=lambda x: random.random())

		 	context = {"study_resources": study_resources}
		 	return render(request, 'study_resource/select_study.html', context)

		else:
			context = {}
			return render(request, 'study_resource/setup_study.html', context)


	else:
		return HttpResponseRedirect(reverse("main:sign_up"))	



def ShareResourceView(request):
	if request.user.is_active == True:
		if request.method == "POST":

			title = request.POST.get("title")
			description = request.POST.get("description")

			study_level = request.POST.get("level")
			study_category = request.POST.get("category")

			content = request.POST.get("content")
			link = request.POST.get("link")

			app_user = AppUser.objects.get(user__pk=request.user.id)
			creator = app_user


			study_resource = StudyResource.objects.create(creator=creator, title=title, description=description, study_level=study_level, study_category=study_category)


			if content != "":
				title = study_resource.title
				content = Content.objects.create(title=title, content=content, contributor=app_user.user.username)
				content.save()
				study_resource_content = StudyResourceContentConnector(study_resource=study_resource, content=content)
				study_resource_content.save()

			study_resource.save()


			return HttpResponseRedirect(reverse("main:index"))

			

		else:
			context = {}
			return render(request, "study_resource/share.html", context)
	else:
		return HttpResponseRedirect(reverse("main:sign_up"))


def ResourceDetailView(request, slug):
	#if request.user.is_active == True:
	study_resource = StudyResource.objects.get(slug=slug)
	context = {"study_resource": study_resource}
	return render(request, "study_resource/detail.html", context)

#	else:
#		return HttpResponseRedirect(reverse("main:sign_up"))

def ContentDetailView(request, content_id):
	if request.user.is_active == True:
		#resource_content = study_resource.contents.get(id=content_id)
		resource_content = Content.objects.get(id=content_id)

		#return HttpResponse(str(resource_content))

		context = {"resource_content": resource_content}
		return render(request, "study_resource/content_detail.html", context)

	else:
		return HttpResponseRedirect(reverse("main:sign_up"))


def ContributeVideoView(request, id):
	if request.user.is_active == True:
		study_resource = StudyResource.objects.get(id=id)

		if request.method == "POST":

			app_user = AppUser.objects.get(user__pk=request.user.id)
			contributor = app_user.user.username
			title = study_resource.title

			try:
				file = request.FILES["study_file"]
				video = Video.objects.create(title=title, video=file, contributor=contributor)
				video.save()

				study_resource_video = StudyResourceVideoConnector(study_resource=study_resource, video=video)
				study_resource_video.save()

			except:
				pass


			return HttpResponseRedirect(reverse("study_resource:contribute_video", args=(study_resource.id,)))


			

		else:
			context = {"study_resource": study_resource}
			return render(request, "study_resource/contribute_video.html", context)

	else:
		return HttpResponseRedirect(reverse("main:sign_up"))



def ContributeImageView(request, id):
	if request.user.is_active == True:
		study_resource = StudyResource.objects.get(id=id)

		if request.method == "POST":

			app_user = AppUser.objects.get(user__pk=request.user.id)
			contributor = app_user.user.username
			title = study_resource.title

			try:
				file = request.FILES["study_file"]
				image = Image.objects.create(title=title, image=file, contributor=contributor)
				image.save()

				study_resource_image = StudyResourceImageConnector(study_resource=study_resource, image=image)
				study_resource_image.save()

			except:
				pass


			return HttpResponseRedirect(reverse("study_resource:contribute_image", args=(study_resource.id,)))


			

		else:
			context = {"study_resource": study_resource}
			return render(request, "study_resource/contribute_image.html", context)

	else:
		return HttpResponseRedirect(reverse("main:sign_up"))


def ContributeEbookView(request, id):
	if request.user.is_active == True:
		study_resource = StudyResource.objects.get(id=id)

		if request.method == "POST":

			app_user = AppUser.objects.get(user__pk=request.user.id)
			contributor = app_user.user.username

			title = study_resource.title

			try:
				file = request.FILES["study_file"]
				ebook = Ebook.objects.create(title=title, ebook=file, contributor=contributor)
				ebook.save()

				study_resource_ebook = StudyResourceEbookConnector(study_resource=study_resource, ebook=ebook)
				study_resource_ebook.save()

			except:
				pass


			return HttpResponseRedirect(reverse("study_resource:contribute_ebook", args=(study_resource.id,)))

			

		else:
			context = {"study_resource": study_resource}
			return render(request, "study_resource/contribute_ebook.html", context)


	else:
		return HttpResponseRedirect(reverse("main:sign_up"))


def ContributeContentView(request, id):
	if request.user.is_active == True:
		study_resource = StudyResource.objects.get(id=id)

		if request.method == "POST":

			content = request.POST.get("content")

			app_user = AppUser.objects.get(user__pk=request.user.id)
			contributor = app_user.user.username

			title = study_resource.title
			
			if content != "":
				content = Content.objects.create(title=title, content=content, contributor=contributor)
				content.save()
				study_resource_content = StudyResourceContentConnector(study_resource=study_resource, content=content)
				study_resource_content.save()

			study_resource.save()


			return HttpResponseRedirect(reverse("study_resource:contribute_content", args=(study_resource.id,)))


		
		else:
			context = {"study_resource": study_resource}
			return render(request, "study_resource/contribute_content.html", context)


	else:
		return HttpResponseRedirect(reverse("main:sign_up"))


def ContributeLinkResourceView(request, id):
	if request.user.is_active == True:
		study_resource = StudyResource.objects.get(id=id)

		if request.method == "POST":


			link = request.POST.get("link")

			app_user = AppUser.objects.get(user__pk=request.user.id)
			contributor = app_user.user.username
			title = study_resource.title

			if link != "":
				link = Link.objects.create(title=title, link=link, contributor=contributor)
				link.save()
				study_resource_link = StudyResourceLinkConnector(study_resource=study_resource, link=link)
				study_resource_link.save()


			study_resource.save()


			return HttpResponseRedirect(reverse("study_resource:contribute_link", args=(study_resource.id,)))

			

		else:
			context = {"study_resource": study_resource}
			return render(request, "study_resource/contribute_to_links.html", context)



	else:
		return HttpResponseRedirect(reverse("main:sign_up"))




def ContributeChatView(request, id):
	if request.user.is_active == True:
		study_resource = StudyResource.objects.get(id=id)

		if request.method == "POST":

			chat = request.POST.get("chat")

			app_user = AppUser.objects.get(user__pk=request.user.id)
			contributor = app_user

			title = study_resource.title

			
			if chat != "":
				chat = Chat.objects.create(title=title, chat=chat, contributor=contributor)
				chat.save()
				study_resource_chat = StudyResourceChatConnector(study_resource=study_resource, chat=chat)
				study_resource_chat.save()

			study_resource.save()

			return HttpResponseRedirect(reverse("study_resource:contribute_chat", args=(study_resource.id,)))

		
		else:
			context = {"study_resource": study_resource}
			return render(request, "study_resource/contribute_chat.html", context)


	else:
		return HttpResponseRedirect(reverse("main:sign_up"))