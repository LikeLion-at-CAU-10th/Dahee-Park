from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def http_response(request):
    if request.method == 'GET':
        return HttpResponse("success GET")


def json_response(request):
    if request.method == 'GET':

        data = {
            'name' : 'Dahee',
            'age' : '23',
            'univ' : 'CAU'
        }

        return JsonResponse(data=data)

    
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        data = {
            'name' : name
        }

        return render(request, 'index.html', context=data)

    else :
        return render(request, 'index.html')