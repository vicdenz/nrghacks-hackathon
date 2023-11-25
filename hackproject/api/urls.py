from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('classrooms/', views.get_classrooms_view, name="notes"),

    path('classrooms/<str:pk>/', views.get_classroom_view, name="note"),
]