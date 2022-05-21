from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('register', views.register_view, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('job', views.job, name='job'),
    path('jobinfo', views.job_info, name='job_info'),
    path('registeruserinjob', views.registerUserInJob, name='registeruserinjob'),
    path('job/view/id=<int:id>', views.job_view, name='job_view'),
    path('closed_job/view/id=<int:id>', views.closed_job_view, name='closed_job_view'),
    path('enterprises', views.enterprises, name='enterprises'),
    path('enterprise/<str:username>/id=<int:enterprise_id>', views.enterprises_view, name='enterprises_view'),
    path('my_jobs', views.my_jobs, name='my_jobs'),
    path('profile', views.profile, name='profile'),
    path('profile/user/edit', views.edit_profile, name='edit_profile'),
    path('announce_job', views.announce_job, name='announce_job'),
    path('announced', views.announced, name='announced'),
    path('user/id=<int:id>/get', views.user_get, name='user_get'),
    path('closejob/job-id=<int:id>', views.closejob, name='closejob'),
    path('closejob/api', views.closejob_api, name='closejob_api'),
    path('usershired/api', views.usershired_api, name='usershired_api'),
]
