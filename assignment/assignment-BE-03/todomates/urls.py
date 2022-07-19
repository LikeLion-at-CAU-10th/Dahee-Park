from django.urls import path

from .views import *


urlpatterns = [
    path('create-category/', create_category, name="create_category"),
    path('get-category-all/', get_category_all, name="get_category_all"),
    path('get-category/<int:id>', get_category, name="get_category"),
    path('create-todo/<int:category_id>', create_todo, name="create_todo")
]