from django.url import path
from profiles_app import views


url_patterns = [
    path('hello-view/', views.ProfileApiView.as_view())
]