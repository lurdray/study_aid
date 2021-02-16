from django.urls import path
from . import views

app_name = "theory"

urlpatterns = [

	path("share-theory-question/", views.ShareTheoryView, name="share_theory"),
	path("edit-theory-question/", views.EditTheoryView, name="edit_theory"),

	path("theory/<str:category>/<str:level>/", views.AllTheoryView, name="all_theory"),
]
