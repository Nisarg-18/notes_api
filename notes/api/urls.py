from django.urls import path
from . import views
urlpatterns=[
    path('',view=views.getRoutes),
    path('notes/',view=views.getNotes),
    path('notes/create/',view=views.createNote),
    path('notes/<str:pk>/update/',view=views.updateNote),
    path('notes/<str:pk>/',view=views.getNote),
    path('notes/<str:pk>/delete',view=views.deleteNote),

]