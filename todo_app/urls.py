from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.task_view,name="result"),
    path('delete/<int:task_id>', views.delete,name="delete"),
    path('update/<int:id>', views.update,name="update"),
    path('home/',views.Tasklistview.as_view(),name="taskview"),
    path('detail/<int:pk>/',views.TaskDetailView.as_view(),name="detail"),
    path('update/<int:pk>/',views.TaskUpdateView.as_view(),name="updatee"),
    path('delete/<int:pk>/',views.TaskDeleteView.as_view(),name="deletee")

]

