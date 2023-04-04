from django.shortcuts import render

from django.urls import path
from .views import apiOverview, userList, newUser, userDetail

urlpatterns = [
	path('', apiOverview, name="api-overview"),
	path('user-list/', userList, name="user-list"),
	path('user-detail/<int:pk>/', userDetail, name="user-detail"),
	path('new-user/', newUser, name="new-user"),
]