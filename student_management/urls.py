"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import  TokenObtainPairView,TokenRefreshView
# from super_admin import views
# from super_admin import api_jobportal
# from .api_jobportal import WhatsAppSendView
from student_management import views
urlpatterns = [
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('login/',views.login_view,name="login" ),
  path('create-user/',views.create_user,name="create_user" ),
  path('universities/', views.add_university, name='university_list'),  # For GET and POST
  path('universities/<int:university_id>/',views.university_detail,name='university_detail'),# For GET,PUT DELETE
  path('universities-courses/', views.universities_with_courses, name='universities_with_courses'),
  
  
  path('create-semester-fees/',views.create_semester_fees,name="create_semester_fees" ),
  path('create-year-fees/', views.create_year_fees, name='create_year_fees'),
  path('get-year-fees/', views.get_year_fees, name='get_year_fees'),

  path('payment-modes/',views.payment_modes,name="payment_modes" ),
  path('payment-modes/<int:id>/', views.payment_mode_detail, name='payment_mode_detail'),
  path('fee-receipt-options/', views.fee_receipt_options, name='fee_receipt_options'),
  path('fee-receipt-options/<int:id>/', views.fee_receipt_option_detail, name='fee_receipt_option_detail'),
  path('bank-names/', views.bank_names, name='bank_names'),
  path('bank-names/<int:id>/', views.bank_name_detail, name='bank_name_detail'),
  path('session-names/', views.session_names, name='session_names'),
  path('session-names/<int:id>/', views.session_name_detail, name='session_name_detail'),
  path('change-password/', views.change_password, name='change_password'),
  path('courses/', views.get_courses_by_university, name='get_courses_by_university'),
  path('streams/', views.get_stream_by_course_one, name='get_streams_by_course'),
  path('substreams/', views.get_substreams_by_university_course_stream, name='get_substreams_by_university_course_stream'),
  path('student-registration/', views.student_registration, name='student_registration'),  
  path('search-by-enrollment-id/', views.search_by_enrollment_id, name='search_by_enrollment_id'),
  path('search-by-student-name/', views.search_by_student_name, name='search_by_student_name'),
  path('create-courses/', views.create_course, name='create_course'),
  path('create-stream/', views.create_stream, name='create_stream'),
  path('create-substream/', views.create_sub_stream, name='create_sub_stream'),
  path('create-subject/', views.create_subject, name='create_subject'),

  path('get-student-course-details/<int:student_id>/',views.get_student_course_details,name='get_student_course_details'),
  path('update-student-course-details/<int:student_id>/',views.update_student_course_details, name='update_student_course_details'),
  # get all courses with there respective university
 
  path('update-course/<int:course_id>/',views.update_course, name='update_course'),
  path('streams/<int:course_id>/', views.get_stream_by_course_two, name='get-stream-by-course'),
  path('update-streams/<int:course_id>/', views.update_streams_by_course, name='update-streams-by-course'),  
  path('update-substreams/<int:stream_id>/', views.update_substreams_by_stream, name='update-substreams-by-stream'),
  
  path('quick-registration/', views.quick_registration, name='quick_registration'),
  path('get_sem_year_by_stream/', views.get_sem_year_by_stream, name='get_sem_year_by_stream'),
  
  path('get_sem_year_by_stream_byname/', views.get_sem_year_by_stream_byname, name='get_sem_year_by_stream_byname'),

  path('fee-receipt-options/', views.get_fee_recipt_option, name='get_fee_receipt_options'),
  path('bank_names/', views.bank_names_list_create, name='bank_names_list_create'),
  path('payment_modes/', views.payment_modes_list_create, name='payment_modes_list_create'),
  path('quick-registered-students/', views.view_quick_registered_students, name='quick_registered_students'),
  path('view_pending_verification_students/', views.view_pending_verification_students, name='view_pending_verification_students'),

  path('registered-students-list/', views.get_student_registration_list, name='get_student_registration_list'),
  
  path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
  path('get-sem-fees/', views.get_sem_fees, name='get_sem_fees'),
  
  #created by ankit to get id of all 
  path('courses-with-id/', views.get_courses_by_university_with_id, name='get_courses_by_university_with_id'),
  path('streams-with-id/', views.get_stream_by_course_with_id, name='get_stream_by_course_with_id'),
  path('substreams-with-id/', views.get_substreams_by_stream_with_id, name='get_substreams_by_university_course_stream_with_id'),

    path('countries/', views.get_country, name='get_country'),
    path('states/', views.get_states, name='get_states'),
    path('cities/', views.get_cities, name='get_cities'),

    path('get-student/<int:enrollment_id>', views.get_student_details, name='get_student_details'),
    path('update-student/<int:enrollment_id>', views.update_student_details, name='update_student_details'),
    # path('upload-student-documents/', views.upload_student_documents, name='upload_student_documents'),
  # path('update-quick-student/<int:enrollment_id>', views.update_quick_student_details, name='update_quick_student_details'),
  
  path('bulk-student-upload/', views.bulk_student_upload, name='bulk_student_upload'),
  path('get_uploaded_student_files/', views.get_uploaded_student_files, name='get-uploaded-student-files'),
  path('delete_student_file_upload/<int:file_id>/', views.delete_student_file_upload, name='delete-student-file-upload'),
  path('download_student_data_excel/', views.download_student_data_excel, name='download-student-data-excel'),

  path('fetch-subject/',views.fetch_subject,name='fetch_subject'),
  path('exams-bulk-upload/', views.bulk_exam_upload, name='bulk_exam_upload'),
  # path('upload_bulk_exam_data/', views.upload_bulk_exam_data, name='upload_bulk_exam_data'),

  path('filter-questions/', views.filter_questions, name='filter_questions'),
  path('fetch_exam/', views.fetch_exam, name='fetch_exam'),
  path('view-assigned-students/', views.view_assigned_students, name='view_assigned_students'),
  path('save_exam_details/', views.save_exam_details, name='save_exam_details'),
  
  path('view_set_examination/', views.view_set_examination, name='view_set_examination'),

  path('set_exam_for_subject/', views.set_exam_for_subject, name='set_exam_for_subject'),
  path('delete_exam_for_student/', views.delete_exam_for_student, name='delete_exam_for_student'),

  path('reassign_student/', views.reassign_student, name='reassign_student'),
  path('get_course_duration/', views.get_course_duration, name='get_course_duration'),
  path('get_all_subjects/', views.get_all_subjects, name='get_all_subjects'),

  path('student_login/', views.student_login, name='student_login'),
  path('download-excel-for-subject/', views.download_excel_for_set_exam_for_subject, name='download_excel_for_set_exam_for_subject'),
  path('all-questions/', views.fetch_questions_based_on_exam_id, name='fetch_questions_based_on_exam_id'),
  path('resend-email/', views.resend_exam_email, name='resend_exam_email'),
  path('examinations/', views.get_result_to_show_based_on_subject, name='get_result_based_on_subject'),
  path('save-submitted-answers/', views.save_all_questions_answers, name='save_all_questions_answers'),
  path('export_to_excel/', views.export_to_excel, name='export_to_excel'),
  path('generate-result/', views.generate_result, name='generate_result'),
  path('show-result/', views.show_result, name='show_result'),

# delete stream substream course and university
  path('delete_university/<int:university_id>/', views.delete_university, name='delete_university'),
  path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
  path('delete_stream/<int:stream_id>/', views.delete_stream, name='delete_stream'),
  path('delete_substream/<int:substream_id>/', views.delete_substream, name='delete_substream'),
  path('delete_subject/<int:subject_id>/', views.delete_subject, name='delete_subject'),  
  
  path('substreams-withid/', views.get_substreams_with_id_by_university_course_stream, name='get_substreams_with_id_by_university_course_stream'),
#---------------------------------------------------------------------------------------------
  path('list_of_all_registered_student/', views.list_of_all_registered_student, name='list_of_all_registered_student'), 
  
  path('list_of_all_cancelled_student/', views.list_of_all_cancelled_student, name='list_of_all_cancelled_student'),
   
  path('get_student_enroll_to_next_year/<int:id>/', views.get_student_enroll_to_next_year, name='get_student_enroll_to_next_year'),

  path('registered_save_enrollment_to_next_semyear/', views.registered_save_enrollment_to_next_semyear, name='save_enrollment_to_next_semyear'),
  
  path("export_students_all_register_excel/",views.export_students_all_register_excel,name="export_students_all_register_excel",),

  path('get_subjects_by_stream/<int:stream_id>/', views.get_subjects_by_stream, name='get_subjects_by_stream'),



  path('update-multiple-subjects/', views.update_multiple_subjects, name='update_multiple_subjects'),
  path('student-cancel/<int:id>/', views.register_cancel_student, name='register_cancel_student'),
  
  path("register-enrollment-new/", views.registered_new_university_enrollment_number, name="register_enrollment_new"),
  path("register-enrollment-old/", views.registered_old_university_enrollment_number, name="register_enrollment_old"),
  path("courier/", views.courier_api, name="courier_api"), 
  
  # path('get_additional_fees/',views.get_additional_fees,name="get_additional_fees"),
  # path('create_additional_fees/', views.create_additional_fees, name='create_additional_fees'),
  # path('update_additional_fees/', views.update_additional_fees, name='update_additional_fees'),
  
  path('result_uploaded_view/', views.result_uploaded_view, name='result_uploaded_view'),

  path('update_result_uploaded_by_student_sem/', views.update_result_uploaded_by_student_sem, name='update_result_uploaded_by_student_sem'),


  path('create_university_exam/', views.create_university_examination, name='create_university_exam'),
  
  path('create_university_reregistration/', views.create_university_reregistration, name='create_university_reregistration'),
  path('get_university_reregistration/', views.get_university_reregistration, name='get_university_reregistration'),
  path('get_paid_fees/', views.get_paid_fees, name='get_paid_fees'),

    path('save_single_answers/', views.save_single_question_answer, name='save_single_answers'),

  path('document-management/<int:enrollment_id>/',views.document_management, name='document_management'),

  path('save_exam_timer/', views.save_exam_timer, name="save_exam_timer"),
  path('get_exam_timer/', views.get_exam_timer, name="get_exam_timer"),
  
  path('save_result_after_exam/', views.save_result_after_exam,name="save_result_after_exam"),
  path('check_exam_result/', views.check_exam_result),
  
  path('check_exam_availability/', views.check_exam_availability, name="check_exam_availability"),

#-----Leads module--------------------------------------
  # path('categories-create/', views.create_category, name='create_category'),
  path('categories-update/<int:pk>/', views.update_category, name='update_category'),
  path('categories/', views.list_categories, name='list_categories'),
  
  path('sources-create/', views.create_source, name='create_source'),
  path('sources-update/<int:pk>/', views.update_source, name='update_source'),
  path('sources/', views.list_sources, name='list_sources'),
  
  path('statuses/', views.list_statuses, name='list_statuses'),
  path('statuses-create/', views.create_status, name='create_status'),
  path('statuses-update/<int:pk>/', views.update_status, name='update_status'),
  
  path('common-lead-labels/', views.list_common_lead_labels, name='list_common_lead_labels'),
  path('common-lead-labels-create/', views.create_common_lead_label, name='create_common_lead_label'),
  path('common-lead-labels-update/<int:pk>/', views.update_common_lead_label, name='update_common_lead_label'),
  
  # path('colors/', views.list_colors, name='list_colors'),
  # path('colors-create/', views.create_color, name='create_color'),
  # path('colors-update/<int:pk>/', views.update_color, name='update_color'),
  path('sync_answers/', views.sync_answers, name='sync_answers'),
  
  path('export_exam_data_to_excel/', views.export_exam_data_to_excel, name='export_exam_data_to_excel'),
  path('fetch_complete_student_data/', views.fetch_complete_student_data_api, name='fetch_complete_student_data'),
  path('view_all_assigned_students_api/', views.view_all_assigned_students_api, name='view_all_assigned_students_api'),
#---------------------Role----------------------------------------------#

  path('get_roles/', views.get_roles, name='view_all_assigned_students_api'),
  path('create_role/', views.create_role, name='create_role'),
  path("roles/save-permissions/", views.save_role_permissions, name="save-role-permissions"),
  path("roles/permissions/<int:role_id>/", views.get_role_permissions, name="get-role-permissions"),
  path("edit_role/<int:role_id>/", views.edit_role, name="edit_role"),
  path('get_role_user/', views.get_role_user, name='get_role_user'),
  path('get_user_dropdown/', views.get_user_dropdown, name='get_user_dropdown'),

  path('create_or_update_user/', views.create_or_update_user, name='create_user'),
  path('get_user/<int:user_id>/', views.get_user_by_id, name='get_user_by_id'),
  path('create_category/', views.create_category, name='create_category'),
  path('get_all_categories/', views.get_all_categories, name='get_all_categories'),
  path('update_category/<int:category_id>/', views.update_category, name='update_category'),
  path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
  path('get_all_sources/', views.get_all_sources, name='get_all_sources'),
  path('create_source/', views.create_source, name='create_source'),
  path('update_source/<int:source_id>/', views.update_source, name='update_source'),
  path('delete_source/<int:source_id>/', views.delete_source, name='delete_source'),
  path('get_all_role_status/', views.get_all_role_status, name='get_all_role_status'),
  path('create_role_status/', views.create_role_status, name='create_role_status'),
  path('update_role_status/<int:role_status_id>/', views.update_role_status, name='update_role_status'),
  path('delete_role_status/<int:role_status_id>/', views.delete_role_status, name='delete_role_status'),  
  path('get_all_lead_label_tags/', views.get_all_lead_label_tags, name='get_all_lead_label_tags'),
  path('create_lead_label_tag/', views.create_lead_label_tag, name='create_lead_label_tag'),
  path('update_lead_label_tag/<int:tag_id>/', views.update_lead_label_tag, name='update_lead_label_tag'),
  path('delete_lead_label_tag/<int:tag_id>/', views.delete_lead_label_tag, name='delete_lead_label_tag'),  
  path('get_all_countries/', views.get_all_countries, name='get_all_countries'),
  path('create_country/', views.create_country, name='create_country'),
  path('update_country/<int:country_id>/', views.update_country, name='update_country'),
  path('delete_country/<int:country_id>/', views.delete_country, name='delete_country'),


  path('states_new/', views.list_states, name='list_states'),
  path('states_new/create/', views.create_state, name='create_state'),
  path('states_new/<int:state_id>/update/', views.update_state, name='update_state'),
  path('states_new/<int:state_id>/delete/', views.delete_state, name='delete_state'),
  
  path('cities/', views.list_cities, name='list_cities'),
  path('cities/create/', views.create_city, name='create_city'),
  path('cities/<int:city_id>/update/', views.update_city, name='update_city'),
  path('cities/<int:city_id>/delete/', views.delete_city, name='delete_city'),

  path("get_user_profile/", views.get_user_profile, name="get_user_profile"),

  path('get_all_colors/', views.get_all_colors, name='get_all_colors'),
  path('create_color/', views.create_color, name='create_color'),
  path('update_color/<int:color_id>/', views.update_color, name='update_color'),
  path('delete_color/<int:color_id>/', views.delete_color, name='delete_color'),
  path("create_lead/", views.create_lead, name="create_lead"),
  path('check_lead_duplicates/', views.check_lead_duplicates, name='check_lead_duplicates'),

  path("role_status_list/", views.role_status_list, name="role_status_list"),
  path("filter_leads_by_status/", views.filter_leads_by_status, name="filter_leads_by_status"),
  path("get_lead_user/", views.get_lead_user, name="get_lead_user"),
  path("update_lead/<int:lead_id>/", views.update_lead, name="update_lead"),
  path("get_lead/<int:lead_id>/", views.get_lead_by_id, name="get_lead"),
  path("get_all_leads/", views.get_all_leads, name="get_all_leads"),

  path("filter_leads/", views.filter_leads, name="filter_leads"),
  path("search_leads_by_mobile/", views.search_leads_by_mobile, name="search_leads_by_mobile"),

  # path("leads/comments/<int:lead_id>/", views.get_lead_comments, name="get_lead_comments"),
  # path("leads/add_comment/<int:lead_id>/", views.create_lead_comment, name="create_lead_comment"),
  path("leads/update_mobiles/<int:lead_id>/", views.update_lead_mobiles, name="update_lead_mobiles"),
  path('edit_user/<int:user_id>/', views.update_user, name='update_user')
  
  
]