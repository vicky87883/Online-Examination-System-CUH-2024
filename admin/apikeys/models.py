from django.db import models

class APIKeys(models.Model):
    students = models.CharField(max_length=255)
    lesson = models.CharField(max_length=255)
    deadline = models.DateField()
    sent = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    actions = models.TextField()

    def __str__(self):
        return f"{self.students} - {self.lesson}"
