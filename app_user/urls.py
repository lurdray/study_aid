from django.urls import path
from . import views

app_name = "app_user"

urlpatterns = [
	
	path("add-app-user/", views.AddAppUserView, name="add_app_user"),
	path("edit-app-user/", views.EditAppUserView, name="edit_app_user"),
]
