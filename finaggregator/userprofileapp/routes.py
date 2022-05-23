from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import UserProfileViewSet

user_profile_router = SimpleRouter()
user_profile_router.register('', UserProfileViewSet, basename='user_profile')

urlpatterns = [
    path('', include(user_profile_router.urls))
]
