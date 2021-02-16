from django.urls import path
from . import views

app_name = "study_resource"

urlpatterns = [
	
	path("share-study-resource/", views.ShareResourceView, name="share_resource"),
	path("study-resource-detail/<int:id>/", views.ResourceDetailView, name="resource_detail"),
	path("contribute-to-resource/<int:id>/", views.ContributeResourceView, name="contribute_resource"),

]
