from traceback import print_tb
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
import json
from django.http import JsonResponse

from .models import *
from .forms import *


def index(request):
    return render(request, 'newjob/index.html')


def login_view(request):
    if request.method == 'POST':
        enterprise = request.POST['enterprise']
        if enterprise == 'true':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("announced"))
            else:
                return render(request, "newjob/login.html", {
                    "message_enterprise": "Invalid username and/or password."
                })
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("my_jobs"))
            else:
                return render(request, "newjob/login.html", {
                    "message_user": "Invalid username and/or password."
                })
    else:
        return render(request, "newjob/login.html")


def register_view(request):
    if request.method == 'POST':
        enterprise = request.POST['enterprise']
        if enterprise == 'true':
            username = request.POST['enterprise_name']
            email = request.POST['email']
            password = request.POST["password"]
            confirmation = request.POST["confirmation"]
            if password != confirmation:
                return render(request, "newjob/register.html", {
                    "message_enterprise": "Passwords must match."
                })
            try:
                user = User.objects.create_user(username, email, password)
                user.enterprise = True
                user.save()
            except IntegrityError:
                return render(request, "newjob/register.html", {
                    "message_enterprise": "Enterprise name or email already taken."
                })
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST["password"]
            confirmation = request.POST["confirmation"]
            if password != confirmation:
                return render(request, "newjob/register.html", {
                    "message_user": "Passwords must match."
                })
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
            except IntegrityError:
                return render(request, "newjob/register.html", {
                    "message_user": "Username or email already taken."
                })
            login(request, user)
            return HttpResponseRedirect(reverse("my_jobs"))
    else:
        return render(request, "newjob/register.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def job(request):
    if request.user.is_authenticated:
        return render(request, "newjob/job.html", {
            'jobs': JobRegister.objects.order_by("-timestamp").all()
        })
    else:
        return HttpResponseRedirect(reverse("login"))


def job_info(request):
    if request.user.is_authenticated:
        allJobs = JobRegister.objects.all()
        return JsonResponse([job.serialize() for job in allJobs], safe=False) 
    else:
        return HttpResponseRedirect(reverse("login"))


def job_view(request, id):
    if request.user.is_authenticated:
        job = JobRegister.objects.get(id=id)
        user_dict = User.objects.get(username=request.user)
        return render(request, 'newjob/job_view.html', {
            'job': job,
            'user_dict': user_dict
        })
    else:
        return HttpResponseRedirect(reverse("login"))


def closed_job_view(request, id):
    if request.user.is_authenticated:
        job = ClosedJobs.objects.get(id=id)
        user_dict = User.objects.get(username=request.user)
        return render(request, 'newjob/closed_job_view.html', {
            'job': job,
            'user_dict': user_dict
        })
    else:
        return HttpResponseRedirect(reverse("login"))


def enterprises(request):
    if request.user.is_authenticated:
        all_enterprises = User.objects.filter(enterprise=True)
        return render(request, "newjob/enterprises.html", {
            'all_enterprises': all_enterprises
        })
    else:
        return HttpResponseRedirect(reverse("login"))


def enterprises_view(request, enterprise_id, username):
    if request.user.is_authenticated:
        enterprise = User.objects.get(id=enterprise_id, username=username)
        enterprise_jobs = JobRegister.objects.filter(business_name=enterprise)
        return render(request, 'newjob/enterprise_view.html', {
            'enterprise': enterprise,
            'enterprise_jobs': enterprise_jobs,
        })
    else:
        return HttpResponseRedirect(reverse("login"))


def my_jobs(request):
    if request.user.is_authenticated:
        return render(request, "newjob/my_jobs.html")
    else:
        return HttpResponseRedirect(reverse("login"))


def profile(request):
    if request.user.is_authenticated:
        return render(request, "newjob/profile.html")
    else:
        return HttpResponseRedirect(reverse("login"))


def edit_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        if request.method == "POST":
            form = FormEditUser(request.POST, request.FILES)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                try:
                    image = form.files['image']
                    if image:
                        user.image = image
                except:
                    pass
                experience = form.cleaned_data['experience']

                if first_name != "" or first_name != None:
                    user.first_name = first_name

                if last_name != "" or last_name != None:
                    user.last_name = last_name
                
                if experience != "" or experience != None:
                    user.experience = experience
                
                try:
                    if experience != "" or experience != None:
                        user.enterprise_description = experience
                except:
                    pass

                user.save()
                if user.enterprise:
                    return HttpResponseRedirect(reverse("index"))
                return HttpResponseRedirect(reverse("profile"))
            return 'ok'
        user = User.objects.get(username=request.user)
        if user.first_name != None and user.last_name != None and user.experience != "":
            form = FormEditUser(initial={
                'experience': user.experience,
                'first_name': user.first_name,
                'last_name': user.last_name
            }, auto_id=False)
        elif user.first_name != None and user.last_name != None:
            form = FormEditUser(initial={
                'first_name': user.first_name,
                'last_name': user.last_name
            }, auto_id=False)
        elif user.experience != "":
            form = FormEditUser(initial={'experience': user.experience}, auto_id=False)
        else:
            form = FormEditUser()
        return render(request, "newjob/edit_profile.html", {
            'user': user,
            'form': form,
        })
    else:
        return HttpResponseRedirect(reverse("login"))


def announce_job(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = JobRegisterForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                minimum_salary = form.cleaned_data['minimum_salary']
                maximum_salary = form.cleaned_data['maximum_salary']
                category = form.cleaned_data['category']
                image = form.files['image']
                business_name = User.objects.get(username=request.user)
                JobRegister(
                    title=title,
                    description=description,
                    minimum_salary=minimum_salary,
                    maximum_salary=maximum_salary,
                    business_name=business_name,
                    category=category,
                    image=image
                ).save()
                return render(request, 'newjob/annouce_job.html', {
                    'message': 'Success! Job successfully annouced',
                    'form': JobRegisterForm()
                })
        return render(request, "newjob/annouce_job.html", {
            'form': JobRegisterForm
        })
    else:
        return HttpResponseRedirect(reverse("login"))


def registerUserInJob(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = json.loads(request.body)
            user_id = data.get("user_id", "")
            job_id = data.get("job_id", "")
            RegisterUserInJob(
                user=User.objects.get(id=user_id),
                job=JobRegister.objects.get(id=job_id)
            ).save()
        
        elif request.method == 'PUT':
            data = json.loads(request.body)
            user_id = data.get("user_id", "")
            job_id = data.get("job_id", "")
            situation = data.get("situation", "")
            user_register = RegisterUserInJob.objects.get(
                user=User.objects.get(id=user_id),
                job=JobRegister.objects.get(id=job_id)
            )
            user_register.situation = situation
            user_register.save()

        allregister = RegisterUserInJob.objects.all()
        return JsonResponse([register.serialize() for register in allregister], safe=False)
    else:
        return HttpResponseRedirect(reverse("login"))


def announced(request):
    if request.user.is_authenticated:
        user = request.user
        jobs =  JobRegister.objects.order_by("-timestamp").filter(business_name=user)
        if user.enterprise:
            return render(request, 'newjob/job.html', {
                'jobs': jobs,
            })
        else:
            return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseRedirect(reverse("login"))


def user_get(request, id):
    user = User.objects.get(id=id)
    return JsonResponse(user.serialize(), safe=False)


def closejob(request, id):
    if request.method == "POST":
        hired = 0
        job_to_close = JobRegister.objects.get(id=id)
        register_users_job_to_close = RegisterUserInJob.objects.filter(job=job_to_close)

        ClosedJobs(
            ex_id_job=id,
            title=job_to_close.title,
            description=job_to_close.description,
            business_name=job_to_close.business_name,
            timestamp=job_to_close.timestamp,
            image=job_to_close.image,
        ).save()

        atualise_job = ClosedJobs.objects.get(ex_id_job=id)

        for register in register_users_job_to_close:
            if register.situation == "Accepted":
                hired += 1
                atualise_job.hired = hired
                enterprise = User.objects.get(id=job_to_close.business_name.id)
                print(enterprise)
                user_hired = UsersHired(user=User.objects.get(id=register.user.id), job=ClosedJobs.objects.get(ex_id_job=id), enterprise=enterprise)
                # tem q ver o pq de n estar salvando aqui
                user_hired.save()

        atualise_job.save()
        job_to_close.delete()
        return HttpResponseRedirect(reverse("index"))
            
    return render(request, "newjob/close_job.html", {
        'job': JobRegister.objects.get(id=id)
    })


def closejob_api(request):
    if request.user.is_authenticated:
        jobs = ClosedJobs.objects.all()
        return JsonResponse([job.serialize() for job in jobs], safe=False)
    else:
        return HttpResponseRedirect(reverse("login"))


def usershired_api(request):
    if request.user.is_authenticated:
        users_hired = UsersHired.objects.all()
        return JsonResponse([user.serialize() for user in users_hired], safe=False)
    else:
        return HttpResponseRedirect(reverse("login"))
