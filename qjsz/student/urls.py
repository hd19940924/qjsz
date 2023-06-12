"""qjsz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
# from maker import views
from student import views
urlpatterns = [

    # path('',views.show,name='show'),
    re_path('^stu_home/',views.stu_home,name = "stu_home"),
    re_path("^stu_major/",views.stu_major,name="stu_major"),
    re_path("^stu_classes/",views.stu_classes,name="stu_classes"),
    re_path("^stu_maker_student/(?P<edit_id>\d+)",views.stu_maker_student,name="stu_maker_student"),
    re_path("^stu_edit/(?P<edit_id>\d+)",views.stu_edit,name="stu_edit"),
    re_path("^stu_classes_self/(?P<edit_id>\d+)",views.stu_classes_self,name="stu_classes_self"),

]
