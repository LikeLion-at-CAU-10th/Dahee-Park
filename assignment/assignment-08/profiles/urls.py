from django.urls import path

from profiles.views import create_profile, get_profile, get_profile_all

urlpatterns = [
    path('create-profile/', create_profile, name="create-profile"),
    path('get-profile-all/', get_profile_all, name="get-profile-all"),
    path('get-profile/<int:id>', get_profile, name="get-profile")
]