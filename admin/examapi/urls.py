# myapp/urls.py
from tkinter.font import names
from django.urls import path
from . import views
from .views import QuestionAPI, UserExamSessionAPI
urlpatterns = [
    path('', views.signup, name='home'),
    path('index',views.index,name='index'),
    path('analytics',views.analytics,name='analytics'),
    path('assignment',views.assignment,name='assignment'),
    path('course-details',views.coursedetails,name='course-details'),
    path('create-course',views.createcourse,name='create-course'),
    path('email',views.email,name='email'),
    path('event',views.event,name='event'),
    path('forgot-password',views.forgotpassword,name='forgot-password'),
    path('index-2',views.index2,name='index-2'),
    path('index-3',views.index3,name='index-3'),
    path('library',views.library,name='library'),
    path('live-class',views.liveclass,name='live-class'),
    path('mentor-courses',views.mentorcourses,name='mentor-courses'),
    path('mentors',views.mentors,name='mentors'),
    path('message',views.message,name='pricing-plan'),
    path('reset-password',views.resetpassword,name='reset-password'),
    path('resources',views.resources,name='resources'),
    path('setting',views.setting,name='setting'),
    path('sign-in',views.signin,name='signin'),
    path('sign-up',views.signup,name='sign-up'),
    path('starred',views.starred,name='starred'),
    path('student-courses',views.studentcourses,name='student-courses'),
    path('students',views.students,name='students'),
    path('two-step-verification',views.twostepverification,name='two-step-verification'),
    path('upload-videos',views.uploadvideos,name='upload-videos'),
    path('verify-email',views.verifyemail,name='verify-email'),
    path('view-details',views.viewdetails,name='view-details'),
    path('about-course',views.aboutcourse,name='about-course'),
    path('create-quiz',views.createquiz,name='create-quiz'),
    path('publish-course',views.publishcourse,name='publish-course'),
    path('pricing-plan',views.pricingplan,name='pricing-plan'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('home', views.home, name='home'),
 path('instructions/', views.instructions_view, name='instructions'),
 path('exam/', views.exam_view, name='exam'),  # Add this line
     path('api/questions/', QuestionAPI.as_view(), name='questions_api'),
    path('api/user_exam_sessions/', UserExamSessionAPI.as_view(), name='user_exam_session_api'),
     path('api/submit_exam/', views.submit_exam, name='submit_exam'),
       path('exam_result/', views.exam_result, name='exam_result'),
]
