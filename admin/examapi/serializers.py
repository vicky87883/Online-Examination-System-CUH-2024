from rest_framework import serializers
from .models import Question, UserExamSession
from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'option1', 'option2', 'option3', 'option4', 'correct_option']

    def validate_correct_option(self, value):
        if not (1 <= value <= 4):
            raise serializers.ValidationError("Correct option must be between 1 and 4.")
        return value

class UserExamSessionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = UserExamSession
        fields = ['id', 'user', 'question', 'selected_option', 'is_marked_for_review']
