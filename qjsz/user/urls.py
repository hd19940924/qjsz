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
from user import views

urlpatterns = [

    # path('',views.show,name='show'),
    re_path('^tea_home/',views.tea_home,name = "tea_home"),
    re_path('^tea_maker_teacher/(?P<edit_id>\d+)',views.tea_maker_teacher,name = "tea_maker_teacher"),
    re_path('^tea_department/',views.tea_department,name = "tea_department"),
    re_path('^tea_maker_student/',views.tea_maker_student,name = "tea_maker_student"),
    re_path('^tea_major/',views.tea_major,name = "tea_major"),
    re_path('^tea_classes/',views.tea_classes,name = "tea_classes"),
    re_path('^tea_add_major/',views.tea_add_major,name = "tea_add_major"),
    re_path('^tea_update_major/(?P<edit_id>\d+)',views.tea_update_major,name = "tea_update_major"),
    re_path('^tea_update_class/(?P<edit_id>\d+)',views.tea_update_class,name = "tea_update_class"),
    re_path('^tea_add_classes/',views.tea_add_classes,name = "tea_add_classes"),
    re_path('^tea_delete_major/(?P<edit_id>\d+)',views.tea_delete_major,name="tea_delete_major"),
    re_path('^tea_delete_class/(?P<edit_id>\d+)',views.tea_delete_class,name="tea_delete_class"),
    re_path('^tea_edit/(?P<edit_id>\d+)',views.tea_edit,name="tea_edit"),
    re_path('^tea_add_student/',views.tea_add_student,name="tea_add_student"),
    re_path('^tea_update_stu/(?P<edit_id>\d+)',views.tea_update_stu,name="tea_update_stu"),
    re_path('^tea_detail_stu/(?P<edit_id>\d+)',views.tea_detail_stu,name="tea_detail_stu"),
    re_path('^tea_delete_stu/(?P<edit_id>\d+)',views.tea_delete_stu,name="tea_delete_stu"),

]
