from django.urls import path
from . import views
urlpatterns=[
    path('',views.welcome,name='welcome'),
    path('verify/',views.sign_log,name="sign_log"),
]
