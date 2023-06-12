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
from maker import views

urlpatterns = [

    path('',views.show,name='show'),
    re_path('^home/',views.home,name = "home"),
    re_path('^maker_student/',views.maker_student,name="maker_student"),
    re_path('^department/',views.department,name="department"),
    re_path('^major/',views.major,name="major"),
    re_path('^classes/',views.classes,name="classes"),
    re_path('^add_student/',views.add_student,name="add_student"),
    re_path('^add_depatment/',views.add_depatment,name="add_depatment"),
    re_path('^add_classes/',views.add_classes,name="add_classes"),
    re_path('^add_major/',views.add_major,name="add_major"),
    re_path('^maker_teacher/',views.maker_teacher,name='maker_teacher'),
    re_path('^add_teacher/',views.add_teacher,name='add_teacher'),
    re_path('^update_tea/(?P<edit_id>\d+)',views.update_tea,name="update_tea"),
    re_path('^update_dep/(?P<edit_id>\d+)',views.update_dep,name='update_dep'),
    re_path('^update_stu/(?P<edit_id>\d+)',views.update_stu,name='update_stu'),
    re_path('^update_major/(?P<edit_id>\d+)',views.update_major,name='update_major'),
    re_path('^update_class/(?P<edit_id>\d+)',views.update_class,name="update_class"),
    re_path('^delete_dep/(?P<edit_id>\d+)',views.delete_dep,name="delete_dep"),
    re_path('^delete_major/(?P<edit_id>\d+)',views.delete_major,name="delete_major"),
    re_path('^delete_class/(?P<edit_id>\d+)',views.delete_class,name="delete_class"),
    re_path('^delete_tea/(?P<edit_id>\d+)',views.delete_tea,name="delete_tea"),
    re_path('^delete_stu/(?P<edit_id>\d+)',views.delete_stu,name="delete_stu"),
    re_path('^detail_stu/(?P<edit_id>\d+)',views.detail_stu,name="detail_stu"),
    re_path('^edit/(?P<e>\w*)',views.edit,name="edit")


]
