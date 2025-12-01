
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


from rest_framework_simplejwt.views import  TokenObtainPairView,TokenRefreshView
urlpatterns = [
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('login/',views.login_view,name="login" ),
  

  # urls for job portal -----------------------------------------------------
  path("add_job_seeker_education/", views.add_job_seeker_education, name="add_job_seeker_education"),
  path("add_work_preferences/", views.add_work_preferences, name="add_work_preferences"),
  path("add_employment_details/", views.add_employment_details, name="add_employment_details"),
  path('post_job/', views.create_job_post, name='post_job'),
  path('get_job_posts/', views.get_job_posts, name='get_job_posts'),
  path('get_job_posts/<int:jobpostid>', views.get_job_post_by_id, name='get_job_posts'),

  path('update_job_post/<int:pk>/', views.update_job_post, name='update_job_post'),
  path('delete_job_post/<int:job_post_id>/', views.delete_job_post, name='delete_job_post'),
  
  path('register_job_seeker/', views.register_job_seeker, name='job-seeker-register'),
  path('authenticate_job_seeker/', views.authenticate_job_seeker,  name='job-seeker-login'),
  
  
  
  
  path('apply_for_job/', views.apply_for_job, name='apply_for_job'),
  path('applications/<int:application_id>/resume/', views.view_application_resume, name='view-application-resume'),
  path('applications_status/<int:application_id>/', views.update_application_status, name='update-application-status'),
  path('applications/', views.get_job_applications, name='get-job-applications'),
  path('jobpost_update_status/<int:jobpost_id>/', views.update_jobpost_status),
  
  
  #------------------------job portal master data--------------------------
  path('departments/', views.jobport_department_list_create, name='jobport-department-list-create'),
  path('departments/<int:pk>/', views.jobport_department_detail, name='jobport-department-detail'),

  # Qualification
  path('qualifications/', views.jobport_qualification_list_create, name='jobport-qualification-list-create'),
  path('qualifications/<int:pk>/', views.jobport_qualification_detail, name='jobport-qualification-detail'),

  # Additional Benefits
  path('benefits/', views.jobport_additionalbenefit_list_create, name='jobport-benefit-list-create'),
  path('benefits/<int:pk>/', views.jobport_additionalbenefit_detail, name='jobport-benefit-detail'),

  # Required Skills
  path('skills/', views.jobport_requiredskill_list_create, name='jobport-skill-list-create'),
  path('skills/<int:pk>/', views.jobport_requiredskill_detail, name='jobport-skill-detail'),

  # Languages
  path('languages/', views.jobport_language_list_create, name='jobport-language-list-create'),
  path('languages/<int:pk>/', views.jobport_language_detail, name='jobport-language-detail'),
  
  # Department Master APIs
  path('departments/', views.jobport_department_list_create, name='jobport-department-list-create'),
  path('departments/<int:pk>/', views.jobport_department_detail, name='jobport-department-detail'),
  
  
  
  
]