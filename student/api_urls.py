from rest_framework import routers
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from student.views import *
from student.views import CheckAPIView,StudentViewSet,LogoutView,LoginView

# holiday_list_view = HolidayViewSet.as_view()

student_list_view = StudentViewSet.as_view({
    "get":"list",
    "post":"create"
})



urlpatterns = [
    url(r'^get/$',student_list_view,name='get_view'),
    url(r'login/$',LoginView.as_view(),name='login_view'),
    url(r'logout/$',LogoutView.as_view(),name='logout_view'),
    url(r'holiday/list/$',CheckAPIView.as_view(),name='holiday_list'),
    url(r'holiday/add/$',CheckAPIView.as_view(),name='holiday_add'),
    url(r'holiday/details/(?P<pk>\d+)/$',CheckAPIView.as_view(),name='holiday_detail')
]