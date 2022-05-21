# What is "New Job"?

New job is a web app that help people find new jobs. In the homepage the user see a introduction of the Web App. When an user clicks on the register button he is redirected to a page that allows him to register as an enterprise or just as an user that want a job. When he clicks on the login button he is redirected to a page to login as an enterprise or as an user.

**Loged as an user:**
  When an user log in, he is redirected to a page to see all jobs that he is registered (opened jobs) and jobs that he is hired (closed jobs). When he clicks on the find job button he is redirected to a page to see all open vacancies, that he can apply for any of them. Clicking on the enterprises button the user see all enterprises registered. He can see the enterprise profile too. He can see his profile clicking on the profile button and edit its clicking on the edit profile button. The user can apply for a job clicking on an announce and clicking on the register button
  
**Loged as an enterprise:**
  When an user log in as an enterprise he is redirected to the homepage. Clicking on announce job button it is displayed a form to announce a new job. When the user, logged in as enterprise, clicks on announced button he is redirect to a page to see all jobs that he announced. Clikcing on profile button he can see his profile and edit it clicking on the edit profile button. Clicking on a job announced, on the botton of the page, the enterprise can see all registered users for that vacancie. For each user registered, is displayed a content to enterprise sees his prifile, accept or reject the user. On click, Asynchronous JavaScript will edit his register in database. Clicking on close job button, the enterprise is redirect to a page to close the job and hire all users accepts for the job.
  
## Distinctiveness and Complexity:
I believe my project satisfies the distinctiveness and complexity requirements because I used all programming languages that I learned on the course, it is a mobile-responsive web app, its use Django on the back-end and JavaScript on the front-end. I think that can easily be used in a real project (with some adjustments) because it's a web app that many people uses in their daily routine to get hired in a job. Thinking about that I decide to develop this awesome web app as my last project.

## What’s contained in each file:
### In newjob/urls.py:
Here is defined the __URL__ configuration for this app.

### In newjob/views.py:
In __views.py__ are all of functions that allows the program run and user find a job. 
  - __login_view:__ The __login_view__ view renders a login form when an user tries to _GET_ the page. If the request method is _POST_, the user is authenticated, logged in, and redirected to another page.

  - __register_view:__ The __register_view__ view is the view that register a new user. Here it is defined whether the user will navigate on the application as enterprise or not. After that, the user is redirected.

  - __logout_view:__ The __logout_view__ logs user out.

  - __job:__ The __job__ view returns all job registers in _JobRegister_ model if user is registered.

  - __job_info:__ The **job_info** view is a _API_ that returns a _JSON_ that contains all informations of all job register.

  - __job_view:__ The **job_view** view returns the information of the job informed by the _URL_.

  - __closed_job_view:__ The **closed_job_view** is the view that allow an enterprise close a job.

  - __enterprises:__ The **enterprises** is the view that allows user see all enterprises registered.

  - __enterprises_view:__ The **enterprises_view** view returns the information of the enterprise informed by the _URL_.

  - __my_jobs:__ The **my_jobs** view returns all jobs that I've registered.

  - __profile:__ The **profile** view allows me to see my profile.

  - __edit_profile:__ The **edit_profile** view allows me to edit my profile.

  - __announce_job:__ The **announce_job** is the view that an enterprise use to announce a job vacancies.

  - __registerUserInJob:__ The **registerUserInJob** view checks whether the request method is _POST_ and register its in _RegisterUserInJob_ model. If request method is _PUT_, the view will get the register and update its. Else the view will return a _JSON_ response that contains all register saved on database.

  - __announced:__ The **announced** view checks if the user is registered as enterprise and return all jobs announced by this enterprise. Else redirect user to index page or login page.

  - __user_get:__ The **user_get** view gets user by the passed id on _URL_ and returns its by a _JSON_ response.

  - __closejob:__ On the **closejob** view, if request method is POST, we delete the job informed by the *URL* of *JobRegister* model, register its in *ClosedJobs* model and register hired users in *UsersHired* model.

  - __closejob_api:__ The **closejob_api** is the view that returns a *API* that contains the registers of all closed jobs.
  
  - __usershired_api:__ The **usershired_api** is the view that returns a *API* that contains the registers of all users that were hired in any job.
 
### In newjob/choices.py:
In __choices.py__ it's some choices of job category. The enterprise is allowed to choose any of them.

### In newjob/static/newjob/js/:
It's all JavaScript documents the web app uses.
  - __color_job.js__: It's responsable for color the all jobs content in the find job page ("/job").

  - __get_registers_users.js__: It's responsable for do the fetch to accept or reject an user on a job, fetch all users registered for the job informed by url and displays it to the enterprise, show info of users registered for that job to enterprise and show to the enterprise all registered users for a job on the page.
  
  -  __image_change.js__: Change the images on index page ("/").
 
  -  __my_jobs.js__: It's responsable for fetch to display the jobs that I am registered (if accept or not) and the closed jobs that I'm accepted. All this jobs will be displayed in _My Jobs_ page ("/my_jobs").
     
  -  __profile.js__: It's responsable for ask user if his want to add a description experience (if his do not have one) and redirect him.
   
  -  __register_user_in_job.js__: It's responsable for do a fetch and verify if the user are alredy registered on a job and will do a fetch to register an user in a job.

## How to run my application:
It's easy, take a look:
  1. Download the code.
  2. Run python manage.py makemigrations newjob to make migrations for the newjob app.
  3. Run python manage.py migrate to apply migrations to your database.
  4. Run python manage.py runserver to you can access the page on the web.
  5. Register an enterprise account or an user account.
  6. Register in a Job (if there is one), if there is not a Job you can login as an enterprise and register one.
