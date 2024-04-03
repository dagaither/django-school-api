from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from .models import Student
from .serializers import StudentAllSerializer, StudentSerializer
# Create your views here.

class All_students(APIView):
    def get(self, request):
        students = Student.objects.all()
        serialized_students = StudentAllSerializer(students, many=True)
        return Response(serialized_students.data)

    def post(self, request):
        data = request.data.copy()
        student = StudentAllSerializer(data=data)
        if student.is_valid():
            student.save()
            return Response(student.data, status=HTTP_201_CREATED)
        return Response(student.errors, status=HTTP_400_BAD_REQUEST)

    
class A_student(APIView):
    def get(self, request, id):
        student = get_object_or_404(Student, id = id)
        return Response(StudentAllSerializer(student).data)
    
    def put(self, request, id):
        student = get_object_or_404(Student, id=id)
        upd_student = StudentAllSerializer(student, data=request.data, partial=True)
        if upd_student.is_valid():
            upd_student.save()
            return Response(upd_student.data, status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT) 
    

class Add_subject(APIView):
    def put(self, request, id, subj):
        student = get_object_or_404(Student, id=id)
        student.add_subject(subject_id=subj)
        return Response(StudentAllSerializer(student).data)


class Remove_subject(APIView):
    def put (self, request, id, subj):
        student = get_object_or_404(Student, id=id)
        student.remove_subject(subject_id=subj)
        return Response(StudentAllSerializer(student).data)



# class Create_student(APIView):
#     def post(self, request):
#         serializer = StudentAllSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)