from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Fuzzy.models import Branch, Student, Semester, Subjects, Marks, Attendance, Technical, Aptitude, FinalEvaluaton

from django.core.serializers import serialize


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        if user.is_active:
            if user.is_staff:
                return redirect('/')
            else:
                return redirect('/show')
    else:
        if request.user.is_active:
            if request.user.is_staff:
                return redirect('/')
            else:
                return redirect('/show')
        else:
            return render(request, 'login.html')


def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        fname = request.POST.get("fname", "")
        lname = request.POST.get("lname", "")
        email = request.POST.get("email", "")
        user = User.objects.create_superuser(username, email=email, password=password)
        user.last_name = lname
        user.first_name = fname
        user.save()
        return redirect('/')

    else:
        return render(request, 'signup.html')


@login_required(login_url='/login')
def dashboard(request):
    branch = Branch.objects.all()
    sem = Semester.objects.all()
    return render(request, 'dashboard.html', {'data': branch, 'sem': sem, })


@login_required(login_url='/login')
def student(request):
    if request.method == 'POST':
        branch = request.POST.get("branch", "")
        stu = Student.objects.filter(Q(branch_id=branch))
        return HttpResponse(serialize('json', stu))


@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login/')
def show(request, idn):
    # stud = Student.objects.get(id=idn)
    # marks = Marks.objects.get(student_id_id=stud)
    sem = Semester.objects.all()

    return render(request, 'show.html', {'sem': sem, "idn": idn})


@login_required(login_url='/login/')
def eligibility(request):
    sem = Semester.objects.all()

    return render(request, 'eligibility.html', {'sem': sem, })


def search(request):
    sem = request.POST.get("sem", "")
    tech1 = request.POST.get("tech", "")
    apti1 = request.POST.get("apti", "")
    stu = Student.objects.all()
    result = []
    for x in stu:
        stud = x.id

        # stu = Marks.objects.filter(Q(student_id_id=stud))
        tech = Technical.objects.filter(Q(sem_id_id=sem) & Q(student_id_id=stud))
        apti = Aptitude.objects.filter(Q(sem_id_id=sem) & Q(student_id_id=stud))
        technical = 0
        aptitude = 0
        for x1 in tech:
            technical += x1.technical

        for x1 in apti:
            aptitude += x1.aptitude

        if technical >= int(tech1) and aptitude >= int(apti1):
            result.append(x)
    # stu1 = Attendance.objects.filter(Q(sem_id_id=sem) & Q(student_id_id=stud))

    # return HttpResponse(str(sem) + str(tech) + str(apti))
    return HttpResponse(serialize('json', result))


# @login_required(login_url='/login/')
def algo(request):
    if request.method == 'POST':
        sem = request.POST.get("sem", "")
        stud = request.POST.get("stud", "")
        stu = Marks.objects.filter(Q(sem_id_id=sem) & Q(student_id_id=stud))
        stu1 = Attendance.objects.filter(Q(sem_id_id=sem) & Q(student_id_id=stud))
        tech = Technical.objects.filter(Q(sem_id_id=sem) & Q(student_id_id=stud))
        apti = Aptitude.objects.filter(Q(sem_id_id=sem) & Q(student_id_id=stud))
        internal = 0
        external = 0
        attendance = 0
        technical = 0
        aptitude = 0
        total = 0
        for x in stu:
            total += 1
            internal += x.internal
            external += x.external

        for x in stu1:
            attendance += x.attendance

        for x in tech:
            technical += x.technical

        for x in apti:
            aptitude += x.aptitude

        return HttpResponse(
            str(internal / total) + "|" + str(external / total) + "|" + str(attendance) + "|" + str(
                technical) + "|" + str(aptitude))


def algo1(request):
    if request.method == 'POST':
        sem = request.POST.get("sem", "")
        stud = request.POST.get("stud", "")
        stu = Marks.objects.filter(Q(sem_id_id=sem) & Q(student_id_id=stud))
        stu1 = Attendance.objects.filter(Q(sem_id_id=sem) & Q(student_id_id=stud))
        tech = Technical.objects.filter(Q(sem_id_id=sem) & Q(student_id_id=stud))
        apti = Aptitude.objects.filter(Q(sem_id_id=sem) & Q(student_id_id=stud))
        internal = 0
        external = 0
        attendance = 0
        technical = 0
        aptitude = 0
        total = 0
        for x in stu:
            total += 1
            internal += x.internal
            external += x.external

        for x in stu1:
            attendance += x.attendance

        internal = float(internal / total)
        external = float(external / total)
        internal_res = ""
        if internal < 50:
            internal_res = "Poor"
        elif 50 < internal < 59.9:
            internal_res = "Average"
        elif 60 < internal < 69.9:
            internal_res = "Good"
        elif 70 < internal < 79.9:
            internal_res = "V. Good"
        elif internal > 80:
            internal_res = "Excellent"

        external_res = ""
        if external < 50:
            external_res = "Poor"
        elif 50 < external < 59.9:
            external_res = "Average"
        elif 60 < external < 69.9:
            external_res = "Good"
        elif 70 < external < 79.9:
            external_res = "V. Good"
        elif external > 80:
            external_res = "Excellent"

        attendance_res = ""

        if attendance < 50:
            attendance_res = "Poor"
        elif 50 < attendance < 54.9:
            attendance_res = "Average"
        if 55 < attendance < 64.9:
            attendance_res = "Good"
        if 65 < attendance < 74.9:
            attendance_res = "V. Good"
        if attendance > 75:
            attendance_res = "Excellent"

        # excellent
        # for x in tech:
        #     technical += x.technical
        #
        # for x in apti:
        #     aptitude += x.aptitude

        stu = FinalEvaluaton.objects.filter(
            Q(internal=internal_res) & Q(external=external_res) & Q(attendance=attendance_res))
        output = ""
        for x in stu:
            output = x.output
        return HttpResponse(output)


def subject(request):
    if request.method == 'POST':
        branch = request.POST.get("branch", "")
        sem = request.POST.get("sem", "")
        stu = Subjects.objects.filter(Q(branch_id_id=branch) & Q(sem_id_id=sem))
        return HttpResponse(serialize('json', stu))


def save_marks(request):
    if request.method == 'POST':
        semid = request.POST.get("semid", "")
        studid = request.POST.get("studentid", "")
        attn = request.POST.get("attn", "")
        tech = request.POST.get("tech", "")
        apti = request.POST.get("apti", "")
        count = request.POST.get("count", "")
        for x in range(0, int(count)):
            subjid = request.POST.get("subjid" + str(x), "")
            intr = request.POST.get("int" + str(x), "")
            ext = request.POST.get("ext" + str(x), "")

            defaults = {'internal': intr, 'external': ext}
            Marks.objects.update_or_create(sem_id_id=semid, student_id_id=studid,
                                           subj_id_id=subjid,
                                           defaults=defaults)
        defaults = {'attendance': attn}
        Attendance.objects.update_or_create(sem_id_id=semid, student_id_id=studid,
                                            defaults=defaults)
        technicals = {'technical': tech}
        Technical.objects.update_or_create(sem_id_id=semid, student_id_id=studid,
                                           defaults=technicals)

        aptitude = {'aptitude': apti}
        Aptitude.objects.update_or_create(sem_id_id=semid, student_id_id=studid,
                                          defaults=aptitude)

        return redirect('/')
