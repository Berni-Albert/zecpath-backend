from django.urls import path
from .views import UserTestAPI, JobListAPI, JobCreateAPI

urlpatterns = [
    path('test/', UserTestAPI.as_view()),
    path('jobs/', JobListAPI.as_view()),
    path('jobs/create/', JobCreateAPI.as_view()),
]