from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from study_resource.models import *

# Create your views here.


def ShareResourceView(request):
	if request.method == "POST":

		title = request.POST.get("title")
		description = request.POST.get("description")

		study_level = request.POST.get("level")
		study_category = request.POST.get("category")

		content = request.POST.get("content")
		link = request.POST.get("link")

		study_resource = StudyResource.objects.create(title=title, description=description, study_level=study_level, study_category=study_category)

		try:
			file = request.FILES["study_file"]
			if type(file) == "image":
				study_resource_image = StudyResourceImageConnector(study_resource=study_resource, image=file)
				study_resource_image.save()

			elif type(file) == "pdf":
				study_resource_ebook = StudyResourceEbookConnector(study_resource=study_resource, ebook=file)
				study_resource_ebook.save()

			else:
				pass



		except:
			pass

		if link != "":
			link = Link.objects.create(title=link, link=link)
			link.save()
			study_resource_link = StudyResourceLinkConnector(study_resource=study_resource, link=link)
			study_resource_link.save()

		if content != "":
			content = Content.objects.create(title=content[10], content=content)
			content.save()
			study_resource_content = StudyResourceContentConnector(study_resource=study_resource, content=content)
			study_resource_content.save()

		study_resource.save()


		return HttpResponseRedirect(reverse("main:index"))

		

	else:
		context = {}
		return render(request, "study_resource/share.html", context)



def ResourceDetailView(request, id):
	
	study_resource = StudyResource.objects.get(id=id)
	context = {"study_resource": study_resource}
	return render(request, "study_resource/detail.html", context)






def ContributeResourceView(request, id):
	study_resource = StudyResource.objects.get(id=id)

	if request.method == "POST":

		content = request.POST.get("content")
		link = request.POST.get("link")

		try:
			file = request.FILES["study_file"]
			if type(file) == "image":
				study_resource_image = StudyResourceImageConnector(study_resource=study_resource, image=file)
				study_resource_image.save()

			elif type(file) == "pdf":
				study_resource_ebook = StudyResourceEbookConnector(study_resource=study_resource, ebook=file)
				study_resource_ebook.save()

			else:
				pass



		except:
			pass

		if link != "":
			link = Link.objects.create(title=link, link=link)
			link.save()
			study_resource_link = StudyResourceLinkConnector(study_resource=study_resource, link=link)
			study_resource_link.save()

		if content != "":
			content = Content.objects.create(content=content)
			content.save()
			study_resource_content = StudyResourceContentConnector(study_resource=study_resource, content=content)
			study_resource_content.save()

		study_resource.save()


		return HttpResponseRedirect(reverse("main:index"))

		

	else:
		context = {"study_resource": study_resource}
		return render(request, "study_resource/contribute.html", context)