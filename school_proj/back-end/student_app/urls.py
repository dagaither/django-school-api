from django.urls import path
from .views import All_students, A_student, Add_subject, Remove_subject

urlpatterns = [
    path("", All_students.as_view(), name='all_students'),
    path("<int:id>/", A_student.as_view(), name="a_student"),
    path("<int:id>/add/<int:subj>/", Add_subject.as_view(), name="add_subject"),
    path("<int:id>/remove/<int:subj>/", Remove_subject.as_view(), name="remove_subject")
]
