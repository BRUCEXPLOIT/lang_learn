from django.urls import path
from . import views
urlpatterns=[
    path('',views.stud_chat,name="student_interface"),

]