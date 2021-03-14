from django.urls import path
from . import views

app_name = "study_resource"

urlpatterns = [
	
	path("setup-study/", views.SetupShareView, name="setup_study"),
	#path("study-select/", views.StudySelectView, name="study_select"),
	path("share-study-resource/", views.ShareResourceView, name="share_resource"),
	path("resource/<slug:slug>/", views.ResourceDetailView, name="resource_detail"),
	#path("contribute-to-ebook/<int:id>/", views.ContributeFileResourceView, name="contribute_ebook"),
	path("contribute-to-ebook/<int:id>/", views.ContributeEbookView, name="contribute_ebook"),
	path("contribute-to-image/<int:id>/", views.ContributeImageView, name="contribute_image"),
	path("contribute-to-video/<int:id>/", views.ContributeVideoView, name="contribute_video"),
	#path("contribute-to-resource/<int:id>/", views.ContributeResourceView, name="contribute_resource"),
	path("contribute-to-content/<int:id>/", views.ContributeContentView, name="contribute_content"),
	path("contribute-to-link/<int:id>/", views.ContributeLinkResourceView, name="contribute_link"),
	path("contribute-to-chat/<int:id>/", views.ContributeChatView, name="contribute_chat"),

	path("content-detail/<int:content_id>/", views.ContentDetailView, name="content_detail"),


]
