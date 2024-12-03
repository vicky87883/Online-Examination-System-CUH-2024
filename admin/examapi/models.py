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
