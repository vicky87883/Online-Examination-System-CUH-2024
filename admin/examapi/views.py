# myapp/views.py
from django.shortcuts import redirect, render
from django.template.context_processors import request
import django.contrib.auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')
    return render(request, 'sign-up.html')
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')
    return render(request, 'sign-in.html')


def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
@login_required
def home(request):
    return render(request, 'index-2.html')
def analytics(request):
    return render(request, 'analytics.html')
def assignment(request):
    return render(request,'assignment.html')
def coursedetails(request):
    return render(request,'course-details.html')
def createcourse(request):
    return render(request,'create-course.html')
def email(request):
    return render(request,'email.html')
def event(request):
    return render(request,'event.html')
def forgotpassword(request):
    return render(request,'forgot-password.html')
def index2(request):
    return render(request,'index-2.html')
def index3(request):
    return render(request,'index-3.html')
def library(request):
    return render(request,'library.html')
def liveclass(request):
    return render(request,'live-class.html')
def mentorcourses(request):
    return render(request,'mentor-courses.html')
def mentors(request):
    return render(request,'mentors.html')
def message(request):
    return render(request,'message.html')
def pricingplan(request):
    return render(request,'pricing-plan.html')
def resources(request):
    return render(request,'resources.html')
def setting(request):
    return render(request,'setting.html')
# authentication program
def signin(request):
    return render(request,'sign-in.html')
def signup(request):
    return render(request,'sign-up.html')
def starred(request):
    return render(request,'starred.html')
def studentcourses(request):
    return render(request,'student-courses.html')
def students(request):
    return render(request,'students.html')
def twostepverification(request):
    return render(request,'two-step-verification.html')
def uploadvideos(request):
    return render(request,'upload-videos.html')
def viewdetails(request):
    return render(request,'view-details.html')
def verifyemail(request):
    return render(request,'verify-email.html')
def resetpassword(request):
    return render(request,'reset-password.html')
def index(request):
        return render(request, 'index.html')  # Render index page for authenticated users
def aboutcourse(request):
    return render(request,'about-course.html')
def createquiz(request):
    return render(request,'create-quiz.html')
def publishcourse(request):
    return render(request,'publish-course.html')