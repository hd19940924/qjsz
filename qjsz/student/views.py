from django.shortcuts import render, redirect
from maker import models

# Create your views here.
def stu_home(request):
    return render(request,'stu_home.html')

def stu_major(request):
    department_queryset = models.Department.objects.all()
    major_queryset = models.Major.objects.all()
    classes_queryset = models.Classes.objects.all()
    return render(request,'stu_major.html',locals())

def stu_classes(request):
    classes_queryset = models.Classes.objects.all()
    major_queryset = models.Major.objects.all()
    return render(request,"stu_classes.html",locals())

def stu_maker_student(request,edit_id):
    student_obj = models.Student.objects.filter(stu_id=edit_id).first()
    department_queryset = models.Department.objects.all()
    major_queryset = models.Major.objects.all()
    classes_queryset = models.Classes.objects.all()
    return render(request,"stu_maker_student.html",locals())

def stu_classes_self(request,edit_id):
    student_obj = models.Student.objects.filter(stu_id=edit_id).first()
    classes_queryset = models.Classes.objects.all()
    major_queryset = models.Major.objects.all()
    return render(request,"stu_classes_self.html",locals())

def stu_edit(request,edit_id):
    if request.method == "POST":
        password = request.POST.get("password")
        if password:
            try:
                password = eval(password)
                student_obj = models.Student.objects.filter(stu_id=edit_id).first()

                student_obj.password = password
                student_obj.save()
                return redirect('stu_home')
            except Exception:
                s = "密码只支持纯数字"
                return render(request, 'stu_edit.html', locals())
        else:
            s = "请输入修改后的密码"
            return render(request, 'stu_edit.html', locals())
    student_obj = models.Student.objects.filter(stu_id=edit_id).first()
    return render(request, 'stu_edit.html', locals())
