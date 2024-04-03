from .models import Grade
from rest_framework import serializers

class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ["grade", "a_subject", "student"]
