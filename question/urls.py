from django.urls import path
from . import views

app_name = "question"

urlpatterns = [

	path("share-question/", views.ShareQuestionView, name="share_question"),
	path("edit-question/", views.EditQuestionView, name="edit_question"),

]
