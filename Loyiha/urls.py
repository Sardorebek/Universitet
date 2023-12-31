from django.contrib import admin
from django.urls import path
from newapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', Salomlash),
    path('', homepage),
    path('fanlar/', fanlar),
    path('yonalish/', yonalishlar),
    path('ustoz/', ustozlar),
    path('hamma_fan_update/<int:son>/', hamma_fan_update),
    path('yonalish_update/<int:son>/', yonalish_update),
]
