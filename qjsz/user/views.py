from django.shortcuts import render,redirect,reverse

from maker import models
# Create your views here.
def tea_home(request):

    return render(request,'tea_home.html',locals())

def tea_add_student(request):
    department_queryset = models.Department.objects.all()
    major_queryset = models.Major.objects.all()
    classes_queryset = models.Classes.objects.all()
    student_queryset = models.Student.objects.all()
    if request.method == "POST":
        stu_id = request.POST.get('stu_id')
        stu_name = request.POST.get('stu_name')
        stu_sex = request.POST.get('stu_sex')
        stu_major = request.POST.get('major_id')
        department = request.POST.get('deparment_id')
        stu_phone = request.POST.get('stu_phone')
        stu_address = request.POST.get('stu_address')
        stu_birthday = request.POST.get('stu_birthday')

        stu_obj = models.Student.objects.filter(stu_id=stu_id)
        if stu_obj:
            msg = "该学生学号已存在请重新录入"
            return render(request, 'tea_add_student.html', locals())
        else:
            models.Student.objects.create(stu_id=stu_id,
                                          stu_name=stu_name,
                                          stu_sex=stu_sex,
                                          stu_major_id=stu_major,
                                          department_id=department,
                                          stu_phone=stu_phone,
                                          stu_address=stu_address,
                                          stu_birthday=stu_birthday,

                                          )
            return redirect('tea_maker_student')
    return render(request,'tea_add_student.html',locals())

def tea_update_stu(request,edit_id):
    department_queryset = models.Department.objects.all()
    major_queryset = models.Major.objects.all()
    student_obj = models.Student.objects.filter(stu_id=edit_id).first()
    if request.method == "POST":
        stu_id = request.POST.get('stu_id')
        stu_name = request.POST.get('stu_name')
        stu_sex = request.POST.get('stu_sex')
        stu_major = request.POST.get('major_id')
        department = request.POST.get('department_id')
        stu_phone = request.POST.get('stu_phone')
        stu_address = request.POST.get('stu_address')
        stu_birthday = request.POST.get('stu_birthday')
        models.Student.objects.filter(stu_id=edit_id).update(
            stu_id=stu_id,
            stu_name=stu_name,
            stu_sex=stu_sex,
            stu_major_id=stu_major,
            department_id=department,
            stu_phone=stu_phone,
            stu_address=stu_address,
            stu_birthday=stu_birthday,
        )
        return redirect('tea_maker_student')
    return render(request,'tea_update_stu.html',locals())

def tea_detail_stu(request,edit_id):
    department_queryset = models.Department.objects.all()
    major_queryset = models.Major.objects.all()
    classes_queryset = models.Classes.objects.all()
    student_obj = models.Student.objects.filter(stu_id=edit_id).first()
    return render(request,'tea_detail_stu.html',locals())

def tea_delete_stu(request,edit_id):
    student_queryset = models.Student.objects.all()
    student_obj = models.Student.objects.filter(stu_id=edit_id).first()
    student_obj.isdeleted = 1
    student_obj.save()
    if student_obj.isdeleted == 1:
        return redirect('tea_maker_student')
    return render(request,'tea_maker_student.html',locals())

def tea_edit(request,edit_id):
    if request.method == "POST":
        password = request.POST.get("password")
        if password:
            try:
                password = eval(password)
                teacher_obj = models.User.objects.filter(userid=edit_id).first()
                teacher_obj.password = password
                teacher_obj.save()
                return redirect('tea_home')
            except Exception:
                s = "密码只支持纯数字"
                return render(request,'tea_edit.html',locals())
        else:
            s = "请输入修改后的密码"
            return render(request, 'tea_edit.html',locals())
    teacher_obj = models.User.objects.filter(userid=edit_id).first()
    return render(request,'tea_edit.html',locals())

def tea_maker_teacher(request,edit_id):
    teacher_obj = models.User.objects.filter(userid=edit_id).first()
    # teacher_queryset = models.User.objects.all()
    return render(request,'tea_maker_teacher.html',locals())

def tea_department(request):
    department_queryset = models.Department.objects.all()
    return render(request,'tea_department.html',locals())

def tea_maker_student(request):
    if request.method == "POST":
        stu_id1 = request.POST.get("stu_id1")
        if stu_id1:
            try:
                stu_id1 = eval(stu_id1)
                student_obj = models.Student.objects.filter(stu_id=stu_id1).first()
                if student_obj:
                    department_queryset = models.Department.objects.all()
                    major_queryset = models.Major.objects.all()
                    classes_queryset = models.Classes.objects.all()
                    return render(request, 'tea_maker_student.html', locals())
                else:
                    errmsg = "你输入学号的学生不存在"
                    department_queryset = models.Department.objects.all()
                    major_queryset = models.Major.objects.all()
                    classes_queryset = models.Classes.objects.all()
                    student_queryset = models.Student.objects.all()
                    return render(request, 'maker_student.html', locals())
            except:
                errmsg = "请输入正确的学号"
                department_queryset = models.Department.objects.all()
                major_queryset = models.Major.objects.all()
                classes_queryset = models.Classes.objects.all()
                student_queryset = models.Student.objects.all()
                return render(request, 'maker_student.html', locals())
        else:
            errmsg = "请输入学号"
            department_queryset = models.Department.objects.all()
            major_queryset = models.Major.objects.all()
            classes_queryset = models.Classes.objects.all()
            student_queryset = models.Student.objects.all()
            return render(request, 'tea_maker_student.html', locals())
    department_queryset = models.Department.objects.all()
    major_queryset = models.Major.objects.all()
    classes_queryset = models.Classes.objects.all()
    student_queryset = models.Student.objects.all()
    return render(request, 'tea_maker_student.html', locals())

def tea_major(request):
    if request.method == "POST":
        major_name1 = request.POST.get("major_name1")
        major_obj = models.Major.objects.filter(major_name=major_name1).first()
        if major_obj:
            department_queryset = models.Department.objects.all()
            return render(request,'tea_major.html',locals())
        else:
            errmsg = "你输入的专业不存在"
            department_queryset = models.Department.objects.all()
            major_queryset = models.Major.objects.all()
            return render(request,'tea_major.html',locals())
    department_queryset = models.Department.objects.all()
    major_queryset = models.Major.objects.all()
    return render(request,"tea_major.html",locals())

def tea_delete_major(request,edit_id):
    major_queryset = models.Major.objects.all()
    major_obj = models.Major.objects.filter(id=edit_id).first()
    major_obj.isdeleted = 1
    major_obj.save()
    if major_obj.isdeleted == 1:
        return redirect('tea_major')
    return render(request, 'tea_major.html', locals())

def tea_classes(request):
    if request.method == "POST":
        classes_name1 = request.POST.get("classes_name1")
        classes_obj = models.Classes.objects.filter(classes_name=classes_name1).first()
        if classes_obj:
            major_queryset = models.Major.objects.all()
            return render(request,'tea_classes.html',locals())
        else:
            errmsg = "你输入的课程不存在"
            classes_queryset = models.Classes.objects.all()
            major_queryset = models.Major.objects.all()
            return render(request,'tea_classes.html',locals())
    major_queryset = models.Major.objects.all()
    classes_queryset = models.Classes.objects.all()
    return render(request,"tea_classes.html",locals())

def tea_delete_class(request,edit_id):
    classes_queryset = models.Classes.objects.all()
    classes_obj = models.Classes.objects.filter(id=edit_id).first()

    classes_obj.isdeleted = 1
    classes_obj.save()

    if classes_obj.isdeleted == 1:
        return redirect('tea_classes')
    return render(request,'tea_classes.html',locals())

def tea_add_major(request):
    msg = ''
    department_queryset = models.Department.objects.all()
    major_queryset = models.Major.objects.all()
    for department_obj in department_queryset:
        print(department_obj.id, department_obj.dm_name, department_obj.dm_dean)
    print(department_queryset)
    if request.method == "POST":
        major_name = request.POST.get("major_name")
        major_teacher = request.POST.get("major_teacher")
        department_id = request.POST.get("deparment")
        print(major_name, major_teacher, department_id)
        major_obj = models.Major.objects.filter(major_name=major_name)
        if major_obj:
            msg = "该专业已存在"
            return render(request, 'tea_add_major.html', locals())
        else:
            models.Major.objects.create(major_name=major_name, major_teacher=major_teacher, department_id=department_id)
            for major_obj in major_queryset:
                print(major_obj.id, major_obj.major_name, major_obj.major_teacher)
            return redirect("tea_major")
    return render(request,'tea_add_major.html',locals())

def tea_update_major(request,edit_id):
    major_obj = models.Major.objects.filter(id=edit_id).first()
    print(major_obj.id, major_obj.major_name, major_obj.major_teacher)
    department_queryset = models.Department.objects.all()
    if request.method == "POST":
        major_name = request.POST.get("major_name")
        major_teacher = request.POST.get("major_teacher")
        department_id = request.POST.get("department_id")
        print(major_name, major_teacher, department_id)
        # major_obj = models.Major.objects.filter(major_name=major_name)
        # if major_obj:
        #     msg= "该专业已存在"
        #     return render(request,'major.html',locals())
        # else:
        models.Major.objects.filter(id=edit_id).update(
            major_name=major_name,
            major_teacher=major_teacher,
            department_id=department_id
        )
        return redirect("tea_major")
    return render(request,'tea_update_major.html',locals())

def tea_add_classes(request):
    msg = ''
    major_queryset = models.Major.objects.all()
    if request.method == "POST":
        classes_name = request.POST.get("classes_name")
        classes_teacher = request.POST.get("classes_teacher")
        major = request.POST.get("major")
        classes_obj = models.Classes.objects.filter(classes_name=classes_name)
        print(classes_name, classes_teacher, major)

        models.Classes.objects.create(classes_name=classes_name, classes_teacher=classes_teacher, major_id=major)
        return redirect("tea_classes")
    return render(request,'tea_add_classes.html',locals())

def tea_update_class(request,edit_id):
    classes_obj = models.Classes.objects.filter(id=edit_id).first()
    major_queryset = models.Major.objects.all()
    if request.method == "POST":
        classes_name = request.POST.get("classes_name")
        classes_teacher = request.POST.get("classes_teacher")
        major = request.POST.get("major")
        models.Classes.objects.filter(id=edit_id).update(
            classes_name=classes_name,
            classes_teacher=classes_teacher,
            major_id=major
        )
        return redirect('tea_classes')
    return render(request,'tea_update_class.html',locals())