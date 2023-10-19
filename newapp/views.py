from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def Salomlash(request):
    return HttpResponse("Salom Dunyo")

def homepage(request):
    return render(request, "home.html")

def fanlar(request):
    if request.method == 'POST':
        Fan.objects.create(
            nom = request.POST.get("f"),
            yonalish = request.POST.get("y"),
            asosiy = request.POST.get("a") == "on"
        )
        return redirect("/fanlar/")
    content = {
        "fanlar": Fan.objects.all()
    }
    return render(request, "hamma_fan.html", content)


def yonalishlar(request):
    if request.method == 'POST':
        Yonalish.objects.create(
            nom = request.POST.get("y_n"),
            aktiv = request.POST.get("a_k") == "on"
        )
        return redirect("/yonalish/")
    content = {
        "yonalish": Fan.objects.all()
    }
    return render(request, "hamma_yonalish.html", content)



def ustozlar(request):
    if request.method == 'POST':
        Ustoz.objects.create(
            ism = request.POST.get("u_i"),
            yosh = request.POST.get("u_y"),
            jins = request.POST.get("jins"),
            daraja = request.POST.get("daraja"),
            fan = Fan.objects.get(id=request.POST.get("f_k"))
        )
        return redirect("/ustoz/")
    content = {
        "ustoz": Ustoz.objects.all()
    }
    return render(request, "ustoz.html", content)

