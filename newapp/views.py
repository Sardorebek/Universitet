from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *

def Salomlash(request):
    return HttpResponse("Salom Dunyo")

def homepage(request):
    return render(request, "home.html")

def fanlar(request):
    if request.method == 'POST':
        forma = FanForm(request.POST)
        if forma.is_valid():
            forma.save()
            # data = forma.cleaned_data
            # Fan.objects.create(
            #     nom = data.get("f"),
            #     yonalish = data.get("y"),
            #     asosiy = data.get("a") == "on"
            # )
        return redirect("/fanlar/")
    content = {
        "fanlar": Fan.objects.all(),
        "forma": FanForm()
    }
    return render(request, "hamma_fan.html", content)


def yonalishlar(request):
    if request.method == 'POST':
        forma = YonalishForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect("/yonalish/")
    content = {
        "yonalish": Fan.objects.all(),
        "forma": YonalishForm()
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

def hamma_fan_update(request, son):
    if request.method == 'POST':

        # Fan.objects.filter(id=son).update(
        #     nom = request.POST.get("f"),
        #     yonalish = request.POST.get("y_o"),
        #     asosiy = request.POST.get("a")
        # )
        return redirect("/fanlar/")
    content = {
        "fan": Fan.objects.get(id=son),
        "forma": FanForm
    }
    return render(request, "hamma_fan_update.html", content)

def yonalish_update(request, son):
    if request.method == 'POST':
        Yonalish.objects.filter(id=son).update(
            nom = request.POST.get("y_n"),
            aktiv = request.POST.get("a_k")
        )
        return redirect("/yonalish/")
    content = {
        "yonal": Yonalish.objects.get(id=son)
    }
    return render(request, "yonalish_update.html", content)