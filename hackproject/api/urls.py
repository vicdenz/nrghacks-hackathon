from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('classrooms/', views.getNotes, name="notes"),

    path('classrooms/<str:pk>/', views.getNote, name="note"),
]