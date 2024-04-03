from django.shortcuts import render, get_object_or_404
from .serializers import Grade, GradeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST

# Create your views here.

class All_grades(APIView):
    def get(self, request):
        grades = Grade.objects.all()
        serialized_grades = GradeSerializer(grades, many=True)
        return Response(serialized_grades.data)
    
    def post(self, request):
        data = request.data.copy()
        grade = GradeSerializer(data=data)
        if grade.is_valid():
            grade.save()
            return Response(grade.data, status=HTTP_201_CREATED)
        return Response(grade.errors, status=HTTP_400_BAD_REQUEST)

class A_grade(APIView):
    def get(self, request, id):
        grade = get_object_or_404(Grade, id=id)
        return Response(GradeSerializer(grade).data)
    
    def put(self, request, id):
        grade = get_object_or_404(Grade, id=id)
        upd_grade = GradeSerializer(grade, data=request.data, partial=True)
        if upd_grade.is_valid():
            upd_grade.save()
            return Response(upd_grade.data, status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        grade = get_object_or_404(Grade, id=id)
        grade.delete()
        return Response(status=HTTP_204_NO_CONTENT)