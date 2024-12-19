# myapp/views.py
from django.shortcuts import redirect, render
from django.template.context_processors import request
import django.contrib.auth
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Question, UserExamSession
from .serializers import QuestionSerializer, UserExamSessionSerializer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response as DRFResponse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Question, UserExamSession
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json  # Add this import at the top of your views.py file
from django.views.decorators.http import require_POST
import json
from rest_framework.response import Response
from .models import Students
from .serializers import StudentSerializer
from .models import APIKeys
from .serializers import APIKeysSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from .models import UploadedFile
from .models import ExamResult, UserExamSession
from .serializers import ExamResultSerializer

import logging
logger = logging.getLogger(__name__)
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
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

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name)
        user.save()
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')
    return render(request, 'sign-up.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST.get('first_name')  # Use get to avoid KeyError

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if first_name == "student":
                login(request, user)
                return redirect('home')  # Render 'home' for students
            elif first_name == "teacher":
                login(request, user)
                return redirect('index-3')  # Render 'home2' for teachers
            else:
                messages.error(request, "Invalid designation!")
                return redirect('login')
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
    # Pass data to the template
    return render(request, 'assignment.html')

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
    
    api_url = "http://127.0.0.1:8000/studentapi/"
    try:
        response = requests.get(api_url)
        logger.info(f"API Response: {response.status_code}")
        if response.status_code == 200:
            student_data = response.json()
            logger.info(f"Fetched API Data: {student_data}")
        else:
          student_data = {"error": "Could not fetch data"}
    except Exception as e:
        logger.error(f"Error fetching API data: {e}")
        student_data = {"error": "Could not fetch data"}
    return render(request, 'students.html', {'student_data': student_data})
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

@login_required
def instructions_view(request):
    return render(request, 'instructions.html')

def exam_view(request):
    return render(request, 'exam.html')

class StartExamView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class SubmitResponseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        question = Question.objects.get(id=data['question_id'])
        session, created = UserExamSession.objects.get_or_create(
            user=request.user,
            question=question,
        )
        session.selected_option = data['selected_option']
        session.is_marked_for_review = data.get('is_marked_for_review', False)
        session.save()
        return Response({"message": "Response saved successfully!"})
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class QuestionAPI(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return DRFResponse(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return DRFResponse(serializer.data, status=status.HTTP_201_CREATED)
        return DRFResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserExamSessionAPI(APIView):
    def get(self, request):
        user_sessions = UserExamSession.objects.filter(user=request.user)
        serializer = UserExamSessionSerializer(user_sessions, many=True)
        return DRFResponse(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        user = request.user
        question = Question.objects.get(id=data['question_id'])
        session, created = UserExamSession.objects.get_or_create(
            user=user,
            question=question,
        )
        session.selected_option = data.get('selected_option')
        session.is_marked_for_review = data.get('is_marked_for_review', False)
        session.save()
        return DRFResponse({
            'message': 'Response saved successfully.',
            'session': UserExamSessionSerializer(session).data,
        }, status=status.HTTP_201_CREATED)
    
def submit_exam(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            correct_answers = 0
            wrong_answers = 0

            for question in data.get('answers', []):
                question_id = question.get('question_id')
                selected_option = question.get('selected_option')

                # Fetch the correct answer for the question from the database
                try:
                    question_obj = Question.objects.get(id=question_id)
                    correct_answer = question_obj.correct_option  # Ensure this field exists in your model
                except Question.DoesNotExist:
                    return JsonResponse({'error': f'Question with ID {question_id} does not exist.'}, status=400)

                # Validate the selected answer
                if str(selected_option) == str(correct_answer):  # Compare as strings to avoid type mismatch
                    correct_answers += 1
                else:
                    wrong_answers += 1

            # Save the result in the session
            request.session['exam_result'] = {
                'correct_answers': correct_answers,
                'wrong_answers': wrong_answers,
                'total_questions': len(data.get('answers', [])),
            }

            # Redirect to the results page
            return JsonResponse({'redirect_url': '/exam_result/'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def exam_result(request):
    # Retrieve the result data from the session
    result = request.session.get('exam_result', {})
    
    if not result:
        return render(request, 'error.html', {'message': 'No result found. Please attempt the exam again.'})
    
    return render(request, 'result.html', {'result': result})


class StudentsListView(APIView):
    # Get all records
    def get(self, request):
        keys = Students.objects.all()
        serializer = StudentSerializer(keys, many=True)
        return Response(serializer.data)

    # Create a new record
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def file_upload_view(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        image = request.FILES.get('image')
        if file:
            UploadedFile.objects.create(file=file, image=image)
        return redirect('file-upload')
    files = UploadedFile.objects.all()
    return render(request, 'resources.html', {'files': files})

