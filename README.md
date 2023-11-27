# School API IX

By the end of this assignment you will have a fully serviceable CRUD API with user authentication capabilities that will allow School staff to easily manage students and scholastic equipment.

## School API Update Capability

In this assignment you will implement the users capability to update Student, Subject, and Grade Data within our Django API through our React application.

## Tasks

- Add a PUT method at the endpoint `http://127.0.0.1:8000/api/v1/subjects/<str:subject>/` that will allow users to update Subject Data.
- Add a PUT method at the endpoint `http://127.0.0.1:8000/api/v1/students/<int:id>/` that will allow user to update Student Data.
- Create a feature that will allow users to ping the endpoint `http://127.0.0.1:8000/api/v1/grades/<int:id>/` that will allow users to update Grade Data.
  