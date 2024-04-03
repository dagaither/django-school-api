from django.shortcuts import render, get_object_or_404
from .serializers import Subject, SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST


# Create your views here.

class All_subjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serialized_subjects = SubjectSerializer(subjects, many=True)
        return Response(serialized_subjects.data)
    
    def post(self, request):
        data = request.data.copy()
        subject = SubjectSerializer(data=data)
        if subject.is_valid():
            subject.save()
            return Response(subject.data, status=HTTP_201_CREATED)
        return Response(subject.errors, status=HTTP_400_BAD_REQUEST)


class A_subject(APIView):
    def get(self, request, subject):
        subject = get_object_or_404(Subject, subject_name = subject.title())
        return Response(SubjectSerializer(subject).data)

    def put(self, request, subject):
        subject = get_object_or_404(Subject, subject_name = subject.title())
        upd_subj = SubjectSerializer(subject, data=request.data, partial=True)
        if upd_subj.is_valid():
            upd_subj.save()
            return Response(upd_subj.data, status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, subject):
        subject = get_object_or_404(Subject, subject_name = subject.title())
        subject.delete()
        return Response(status=HTTP_204_NO_CONTENT)
        