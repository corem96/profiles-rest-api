from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_app import views


router = DefaultRouter()
router.register('profiles-viewset', views.ProfileViewSet, base_name='profile-viewset')
router.register('profiles', views.UserProfileViewSet)


urlpatterns = [
    path('profiles-view/', views.ProfileApiView.as_view()),
    path('', include(router.urls))
]
