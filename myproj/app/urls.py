from django.contrib import admin
from django.urls import path,include
from .views import Companyviewsets,Employeesviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies',Companyviewsets)
router.register(r'employees',Employeesviewsets)


urlpatterns = [
      path('', include(router.urls)),
 ]