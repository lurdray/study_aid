from django.urls import path
from . import views

app_name = "cbt"

urlpatterns = [
	
	path("setup-cbt/", views.SetupCbtView, name="setup_cbt"),
	path("take-cbt/<int:cbt_id>/", views.TakeCbtView, name="take_cbt"),
	path("complete-cbt/<int:cbt_id>/complete/", views.CompleteCbtView, name="complete_cbt"),

]
