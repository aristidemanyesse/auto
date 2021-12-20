from django.shortcuts import render

# Create your views here.


def home(request):
    datas = {}
    return render(request, "master/pages/home.html", datas)

