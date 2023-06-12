from django.shortcuts import render,HttpResponse,redirect,reverse
from maker import models
from user import urls
from student import urls
# Create your views here.

def show(request):
    errmsg = ""
    if request.method == "POST":
        seltype = request.POST.get("seltype")
        if seltype == "管理员":
            username = request.POST.get("username")
            password = request.POST.get("password")
            try:
                maker_obj = models.Maker.objects.filter(name=username).first()
            except:
                return render(request, 'show.html', {"errmsg": "请输入账号","username":username,"password":password})
            if maker_obj:
                if password == maker_obj.password:
                    request.session['username'] = username
                    return redirect(f"%s?username={username}" %reverse('home'))
                    # return render(request,'home.html',locals())
                else:
                    return render(request,'show.html',{"errmsg":"密码错误","username":username,"password":password})
            else:
                return render(request,'show.html',{"errmsg":"用户名错误","username":username,"password":password})
        elif seltype=="教师":
                userid = request.POST.get("username")
                password = request.POST.get("password")
                try:
                    user_obj = models.User.objects.filter(userid=userid).first()
                except:
                    return render(request, 'show.html', {"errmsg": "请输入账号","username":userid,"password":password})
                if user_obj:
                    try:
                        int(password)
                    except:
                        return render(request, 'show.html', {"errmsg": "请输入密码"})
                    if int(password) == user_obj.password:
                        request.session['userid'] = userid
                        return redirect(f"%s?username={userid}" %reverse('tea_home'))

                    else:
                        return render(request, 'show.html', {"errmsg": "密码错误"})
                else:
                    return render(request, 'show.html', {"errmsg": "用户名错误"})
        else:
            stu_id = request.POST.get("username")
            password = request.POST.get("password")
            try:
                student_obj = models.Student.objects.filter(stu_id=stu_id).first()
            except:
                return render(request, 'show.html', {"errmsg": "请输入账号","username":stu_id,"password":password})
            if student_obj:
                try:
                    int(password)
                except:
                    return render(request, 'show.html', {"errmsg": "请输入密码","username":stu_id,"password":password})
                if int(password) == student_obj.password:
                    request.session['stu_id'] = stu_id
                    return redirect(f"%s?username={stu_id}" % reverse('stu_home'))
                else:
                    return render(request, 'show.html', {"errmsg": "密码错误","username":stu_id,"password":password})
            else:
                return render(request, 'show.html', {"errmsg": "用户名错误","username":stu_id,"password":password})

    return render(request, 'show.html')

def edit(request,e):
    maker_obj = models.Maker.objects.filter(name=e).first()
    if request.method == "POST":
        password = request.POST.get("password")

        maker_obj.password = password
        maker_obj.save()
        return redirect('home')
    return render(request,"edit.html",locals())

def maker_student(request):
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
                    return render(request,'maker_student.html',locals())
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
            return render(request,'maker_student.html',locals())
    department_queryset = models.Department.objects.all()
    major_queryset = models.Major.objects.all()
    classes_queryset = models.Classes.objects.all()
    student_queryset = models.Student.objects.all()
    return render(request,'maker_student.html',locals())

def home(request):
    return render(request,"home.html")

def department(request):
    if request.method == "POST":
        dep_name = request.POST.get("dm_name1")
        department_obj = models.Department.objects.filter(dm_name=dep_name).first()
        if department_obj:
            return render(request,'department.html',locals())
        else:
            errmsg = "你输入的院系不存在"
            department_queryset = models.Department.objects.all()
            return render(request,'department.html',locals())
    department_queryset = models.Department.objects.all()
    return render(request, "department.html", locals())

def major(request):
    if request.method == "POST":
        major_name1 = request.POST.get("major_name1")
        major_obj = models.Major.objects.filter(major_name=major_name1).first()
        if major_obj:
            department_queryset = models.Department.objects.all()
            return render(request,'major.html',locals())
        else:
            errmsg = "你输入的专业不存在"
            department_queryset = models.Department.objects.all()
            major_queryset = models.Major.objects.all()
            return render(request,'major.html',locals())
    department_queryset = models.Department.objects.all()
    major_queryset = models.Major.objects.all()
    return render(request,"major.html",locals())

def classes(request):
    if request.method == "POST":
        classes_name1 = request.POST.get("classes_name1")
        classes_obj = models.Classes.objects.filter(classes_name=classes_name1).first()
        if classes_obj:
            major_queryset = models.Major.objects.all()
            return render(request,'classes.html',locals())
        else:
            errmsg = "你输入的课程不存在"
            classes_queryset = models.Classes.objects.all()
            major_queryset = models.Major.objects.all()
            return render(request,'classes.html',locals())
    major_queryset = models.Major.objects.all()
    classes_queryset = models.Classes.objects.all()
    return render(request,"classes.html",locals())

def add_student(request):
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
            return render(request, 'add_student.html', locals())
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
            return redirect('maker_student')
    return render(request,"add_student.html",locals())

def update_stu(request,edit_id):
    department_queryset = models.Department.objects.all()
    major_queryset = models.Major.objects.all()
    student_obj = models.Student.objects.filter(stu_id=edit_id).first()
    if request.method == "POST":
        # userid = request.POST.get("userid")
        stu_id = request.POST.get('stu_id')
        stu_name = request.POST.get('stu_name')
        stu_sex = request.POST.get('stu_sex')
        stu_major = request.POST.get('major_id')
        department = request.POST.get('department_id')
        stu_phone = request.POST.get('stu_phone')
        stu_address = request.POST.get('stu_address')
        stu_birthday = request.POST.get('stu_birthday')
        models.Student.objects.filter(stu_id=edit_id).update(
            stu_id = stu_id,
            stu_name=stu_name,
            stu_sex=stu_sex,
            stu_major_id=stu_major,
            department_id=department,
            stu_phone=stu_phone,
            stu_address=stu_address,
            stu_birthday=stu_birthday,
        )
        return redirect('maker_student')

    return render(request,'update_stu.html',locals())

def delete_stu(request,edit_id):
    student_queryset = models.Student.objects.all()
    student_obj = models.Student.objects.filter(stu_id=edit_id).first()
    student_obj.isdeleted = 1
    student_obj.save()
    if student_obj.isdeleted == 1:
        return redirect('maker_student')
    return render(request,'maker_student.html',locals())

def add_depatment(request):
    msg=''
    department_queryset = models.Department.objects.all()
    if request.method == "POST":
        dm_name = request.POST.get("dm_name")
        dm_dean = request.POST.get("dm_dean")
        dm_phone = request.POST.get("dm_phone")
        department_obj = models.Department.objects.filter(dm_name=dm_name)
        if department_obj:
            msg = "该院系已存在，请重新添加"
            return render(request,'add_depatment.html',locals())
        else:
            print(dm_name, dm_dean, dm_phone)
            models.Department.objects.create(dm_name=dm_name, dm_dean=dm_dean, dm_phone=dm_phone)
            return redirect('department')
    return render(request, "add_depatment.html", locals())

def add_classes(request):
    msg = ''
    major_queryset = models.Major.objects.all()
    if request.method == "POST":
        classes_name = request.POST.get("classes_name")
        classes_teacher = request.POST.get("classes_teacher")
        major = request.POST.get("major")
        classes_obj = models.Classes.objects.filter(classes_name=classes_name)
        print(classes_name,classes_teacher,major)

        models.Classes.objects.create(classes_name=classes_name,classes_teacher=classes_teacher,major_id=major)
        return redirect("classes")

    return render(request,"add_classes.html",locals())

def add_major(request):
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
            msg= "该专业已存在"
            return render(request,'add_major.html',locals())
        else:
            models.Major.objects.create(major_name=major_name, major_teacher=major_teacher, department_id=department_id)
            for major_obj in major_queryset:
                print(major_obj.id, major_obj.major_name, major_obj.major_teacher)
            return redirect("major")
    return render(request, 'add_major.html', locals())

def maker_teacher(request):
    if request.method == "POST":
        userid1 = request.POST.get("userid1")
        if userid1:
            userid1 = eval(userid1)
            teacher_obj = models.User.objects.filter(userid=userid1).first()
            if teacher_obj:
                # teacher_queryset = models.User.objects.all()
                return render(request,'maker_teacher.html',locals())
            else:
                errmsg = "你输入教师号的教师不存在"
                teacher_queryset = models.User.objects.all()
                return render(request,'maker_teacher.html',locals())
        else:
            errmsg = "请输入教师号"
            teacher_queryset = models.User.objects.all()
            return render(request, 'maker_teacher.html', locals())
    teacher_queryset = models.User.objects.all()
    return render(request,'maker_teacher.html',locals())

def add_teacher(request):
    if request.method=="POST":
        userid = request.POST.get("userid")
        username = request.POST.get("username")
        # age = request.POST.get("age")
        usersex = request.POST.get("usersex")
        other = request.POST.get("other")
        user_obj = models.User.objects.filter(userid=userid)
        if user_obj:
            msg = "该教师号已存在请重新录入"
            return render(request, 'add_teacher.html', locals())
        else:
            models.User.objects.create(userid=userid,username=username,usersex=usersex,other=other)
            return redirect('maker_teacher')
    return render(request,'add_teacher.html',locals())

def update_tea(request,edit_id):
    user_obj = models.User.objects.filter(userid=edit_id).first()
    if request.method == "POST":
        # userid = request.POST.get("userid")
        username = request.POST.get("username")
        # age = request.POST.get("age")
        usersex = request.POST.get("usersex")
        other = request.POST.get("other")
        models.User.objects.filter(userid=edit_id).update(
            username=username,

            usersex = usersex,
            other = other
        )
        return redirect('maker_teacher')
    return render(request,'update_tea.html',locals())

def detail_stu(request,edit_id):
    department_queryset = models.Department.objects.all()
    major_queryset = models.Major.objects.all()
    classes_queryset = models.Classes.objects.all()
    student_obj = models.Student.objects.filter(stu_id=edit_id).first()
    return render(request,'detail_stu.html',locals())

def update_dep(request,edit_id):
    department_obj = models.Department.objects.filter(id=edit_id).first()
    if request.method == "POST":
        dm_name = request.POST.get("dm_name")
        dm_dean = request.POST.get("dm_dean")
        dm_phone = request.POST.get("dm_phone")
        models.Department.objects.filter(id=edit_id).update(
                                    dm_name=dm_name,
                                    dm_dean=dm_dean,
                                    dm_phone=dm_phone)
        return redirect('department')
    return render(request,'update_dep.html',locals())

def update_major(request,edit_id):
    major_obj = models.Major.objects.filter(id=edit_id).first()
    print(major_obj.id,major_obj.major_name,major_obj.major_teacher)
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
        return redirect("major")
    return render(request,'update_major.html',locals())

def update_class(request,edit_id):
    classes_obj = models.Classes.objects.filter(id=edit_id).first()
    major_queryset = models.Major.objects.all()
    if request.method=="POST":
        classes_name = request.POST.get("classes_name")
        classes_teacher = request.POST.get("classes_teacher")
        major = request.POST.get("major")
        models.Classes.objects.filter(id=edit_id).update(
        classes_name=classes_name,
        classes_teacher=classes_teacher,
        major_id=major
    )
        return redirect('classes')
    return render(request,'update_class.html',locals())

def delete_dep(request,edit_id):
    department_queryset = models.Department.objects.all()
    department_obj = models.Department.objects.filter(id=edit_id).first()
    # print(department_obj.isdeleted)
    department_obj.isdeleted = 1
    department_obj.save()
    # print(department_obj.isdeleted)
    if department_obj.isdeleted ==1:
        return redirect('department')
    return render(request,'department.html',locals())

def delete_major(request,edit_id):
    major_queryset = models.Major.objects.all()
    major_obj = models.Major.objects.filter(id=edit_id).first()

    major_obj.isdeleted = 1
    major_obj.save()

    if major_obj.isdeleted == 1:
        return redirect('major')
    return render(request,'major.html',locals())

def delete_class(request,edit_id):
    classes_queryset = models.Classes.objects.all()
    classes_obj = models.Classes.objects.filter(id=edit_id).first()

    classes_obj.isdeleted = 1
    classes_obj.save()

    if classes_obj.isdeleted == 1:
        return redirect('classes')
    return render(request,'classes.html',locals())

def delete_tea(request,edit_id):
    teacher_queryset = models.User.objects.all()
    teacher_obj = models.User.objects.filter(userid=edit_id).first()

    teacher_obj.isdeleted = 1
    teacher_obj.save()

    if teacher_obj.isdeleted == 1:
        return redirect('maker_teacher')
    return render(request,'maker_teacher.html',locals())








