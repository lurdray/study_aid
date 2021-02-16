from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

path("sign-in/", views.SignInView, name="sign_in"),
path("sign-up/", views.SignUpView, name="sign_up"),

path("userlogout/", views.UserLogoutView, name="userlogout"),

path("whatever/", views.UserLogoutView, name="time_up_submit"),
path("", views.IndexView, name="index"),

]
