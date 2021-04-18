from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

path("search", views.SearchView, name="search"),

path("sign-in/", views.SignInView, name="sign_in"),
path("sign-up/", views.SignUpView, name="sign_up"),
#path("landing-page/", views.LandingPageView, name="landing_page"),

path("profile/", views.ProfileView, name="profile"),

path("userlogout/", views.UserLogoutView, name="sign_out"),

path("whatever/", views.UserLogoutView, name="time_up_submit"),
path("", views.IndexView, name="index"),
path("about/", views.AboutView, name="about"),
path('contact/', views.contact, name='contact'),
path('all_contacts/', views.all_contacts, name='all_contacts'),

]
