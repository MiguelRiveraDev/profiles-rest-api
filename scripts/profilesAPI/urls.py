from django.urls import path
from profilesAPI import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]