from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.IntegerField()  # 1, 2, 3, or 4

    def __str__(self):
        return self.text

class UserExamSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.IntegerField(null=True, blank=True)  # User's answer
    is_marked_for_review = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.question.text[:20]}"

class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    students = models.CharField(max_length=255)
    emailid = models.CharField(max_length=255)
    courses = models.CharField(max_length=255)
    certificate = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    actions = models.TextField()

    def __str__(self):
        return f"{self.students} - {self.emailid}"

class APIKeys(models.Model):
    students = models.CharField(max_length=255)
    lesson = models.CharField(max_length=255)
    deadline = models.DateField()
    sent = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    actions = models.TextField()

    def __str__(self):
        return f"{self.students} - {self.lesson}"

class UploadedFile(models.Model):
    name = models.CharField(max_length=255,null=True)
    file = models.FileField(upload_to='uploads/files/')
    image = models.ImageField(upload_to='uploads/images/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ExamResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Use a foreign key to the User model
    total_questions = models.IntegerField(null=True)
    correct_answers = models.IntegerField(null=True)
    wrong_answers = models.IntegerField(null=True)
    score_percentage = models.FloatField(null=True)

    def __str__(self):
        return f"{self.user.username} - {self.score_percentage}%"
    
