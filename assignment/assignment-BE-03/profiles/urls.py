from django.urls import path

from profiles.views import create_profile, get_profile, get_profile_all, create_class, get_class, get_class_all

urlpatterns = [
    path('create-profile/', create_profile, name="create-profile"),
    path('get-profile-all/', get_profile_all, name="get-profile-all"),
    path('get-profile/<int:id>', get_profile, name="get-profile"),
    path('create-class/<int:profile_id>', create_class, name="create-class"),
    path('get-class-all/', get_class_all, name="get-class-all"),
    path('get-class/<int:id>', get_class, name="get-class")
]