import json
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import JsonResponse
from .models import *



# Create your views here.

def create_profile(requests):
    if requests.method == 'POST':

        body = json.loads(requests.body.decode('utf-8'))

        new_profile = Profile.objects.create(
            name = body['name'],
            age = body['age'],
            phone = body['phone']
        )

        new_profile_json = {
            "id" : new_profile.id,
            "name" : new_profile.name,
            "age" : new_profile.age,
            "phone" : new_profile.phone,
        }

        return JsonResponse({
            "status" : 200,
                "success" : True,
                "message" : "생성 성공",
                "data" : new_profile_json
        })
    
    return JsonResponse({
        "status" : 405,
            "success" : False,
            "message" : "생성 실패",
            "data" : None
    })


def get_profile_all(requests):
    if requests.method == "GET":
        profile_all = Profile.objects.all()


        profile_json_all = []
        for profile in profile_all:
            profile_json = {
                "id": profile.id,
                "name":profile.name,
                "age":profile.age,
                "phone":profile.phone,
            }
            profile_json_all.append(profile_json)

        return JsonResponse({
                "status" : 200,
                "success" : True,
                "message" : "생성 성공",
                "data" : profile_json_all
        })
            

    return JsonResponse({
    "status" : 405,
        "success" : False,
        "message" : "생성 실패",
        "data" : None
    })


def get_profile(request, id):
    if request.method == "GET":
        profile = get_object_or_404(Profile, pk = id)
        profile_json = {
            "id": profile.id,
            "name": profile.name,
            "age" : profile.age,
            "phone" : profile.phone,
        }

        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "생성 성공",
            "data" : profile_json
        })

    return JsonResponse({
        "status" : 405,
            "success" : False,
            "message" : "생성 실패",
            "data" : None
    })