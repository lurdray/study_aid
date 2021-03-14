from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from study_resource.models import StudyResource


class StaticViewSitemap(Sitemap):
	changefreq = "always"
	
	def items(self):
		return ["main:about"]
		
	def location(self, item):
		return reverse(item)


class StudyResourceSitemap(Sitemap):
	
	def items(self):
		return StudyResource.objects.all()