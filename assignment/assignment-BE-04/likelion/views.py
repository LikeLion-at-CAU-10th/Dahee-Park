from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.decorators.http import require_http_methods
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def likelion(request):
    return render(request, "likelion/likelion.html")


@require_http_methods(["POST", "GET"])
@login_required
def likelion_form_create(request):
    form = LikeLionCreateForm()
    context = {
            "form" : form,
            "word" : "다시 입력하세요."
        }
    print(request.method)
    if request.method == "POST":
        create_form = LikeLionCreateForm(request.POST)
        print(create_form.is_valid())
        if create_form.is_valid():
            likelion = create_form.save()
            likelion.save()
            return HttpResponseRedirect('list')
        else:        
            return render(request, "likelion/likelion_main.html",context=context)
    else:
        return render(request, "likelion/likelion_main.html", context=context)


@require_http_methods(["GET"])
def likelion_list(request, id):
    likelion = get_object_or_404(LikeLion, pk=id)

@require_http_methods(['GET'])
def likelion_list_all(request, id):
    print("request.method :", request.method)
    try:
        likelions = LikeLion.objects.all()
        likelions = LikeLion.objects.get(id=id)
        print(likelions)
    except LikeLion.DoesNotExist:
        return('likelion')
    #likelions = LikeLion.objects.filter()
    context = {
        "likelions": likelions
    }

    return render(request, "likelion/likelion_list.html", context=context)


class LikeLionCreateView(CreateView):
    model = LikeLion
    fields = "__all__"
    success_url = "/likelion"


class LikeLionListView(ListView):
    model = LikeLion
    paginate_by = 30
    #ordering = ['-id']
    ordering = ['name']


class LikeLionDeleteView(DeleteView):
    model = LikeLion
    success_url = "/likelion"


class LikeLionUpdateView(UpdateView):
    model = LikeLion
    fields = "__all__"
    template_name_suffix= '_update_form'
    success_url = "/likelion"
