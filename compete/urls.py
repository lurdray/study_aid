from django.urls import path
from . import views

app_name = "compete"

urlpatterns = [

	path("setup-compete/", views.SetupCompeteView, name="compete"),
	path("result/", views.ResultView, name="result"),
	path("result-detail/<int:id>/", views.ResultDetailView, name="result_detail"),
	path("join-compete", views.JoinCompeteView, name="join_compete"),

]

