from django.urls import path
from . import views
from .views import login_user,logout_user

urlpatterns = [
    path("", views.index, name="Home"),    
    path("about/", views.about, name="About"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout")
    ]
