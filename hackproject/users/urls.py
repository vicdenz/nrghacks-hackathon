from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("sign-up/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
]