import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *

# Create your views here.
def create_category(request):
    if request.method == "POST":

        body = json.loads(request.body.decode('utf-8'))
        
        new_category = Category.objects.create(
            title = body['title'],
            view_auth = body['view_auth'],
            color = body['color']
        )

        new_category_json = {
            "id" : new_category.id,
            "title" : new_category.title,
            "view_auth" : new_category.view_auth,
            "color" : new_category.color,
            "pup_date" : new_category.pup_date,
        }

        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "생성 성공",
            "data" : new_category_json
        })

    return JsonResponse({
        "status" : 405,
            "success" : False,
            "message" : "생성 실패",
            "data" : None
    })


def get_category_all(requests):
    if requests.method == "GET":
        category_all = Category.objects.all()

        category_json_all=[]
        for category in category_all:
            category_json = {
                "id" : category.id,
                "title" : category.title,
                "view_auth" : category.view_auth,
                "color" : category.color,
                "pup_date" : category.pup_date,
            }
            category_json_all.append(category_json)

        return JsonResponse({
        "status" : 200,
        "success" : True,
        "message" : "생성 성공",
        "data" : category_json_all
        })

    return JsonResponse({
        "status" : 405,
            "success" : False,
            "message" : "생성 실패",
            "data" : None
    })


def get_category(requests, id):

    if requests.method == "GET":
        category = get_object_or_404(Category, pk = id)
        category_json = {
                "id" : category.id,
                "title" : category.title,
                "view_auth" : category.view_auth,
                "color" : category.color,
                "pup_date" : category.pup_date,
            }

        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "생성 성공",
            "data" : get_category
        })

    return JsonResponse({
        "status" : 405,
            "success" : False,
            "message" : "생성 실패",
            "data" : None
    })


def create_todo(request, category_id):
    if request.method == "POST":

        body = request.POST
        img = request.FILES['thumb_nail']
        
        new_todo = Todo.objects.create(
            category = get_object_or_404(Category, pk = category_id),
            content = body['content'],
            thumb_nail = img
        )

        new_todo_json = {
            "id" : new_todo.id,
            "content" : new_todo.content,
            "thumb_nail" : '/media/' + str(new_todo.thumb_nail),
            "pup_date" : new_todo.pup_date,
        }

        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "생성 성공",
            "data" : new_todo_json
        })

    return JsonResponse({
        "status" : 405,
            "success" : False,
            "message" : "생성 실패",
            "data" : None
    })