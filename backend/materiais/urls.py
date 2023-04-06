from django.shortcuts import render

from django.urls import path
from .views import (
		apiOverview, 
        userList, 
        newUser, 
        userDetail,
        materialList,
        materialDetail, 
        createMaterial,
        commentDetail,
        commentList, 
        createComment,
        updateUser,
        deleteUser,
        updateMaterial,
        deleteMaterial,
        updateComment,
        deleteComment,
)
    

urlpatterns = [
	path('', apiOverview, name="api-overview"),
	path('user-list/', userList, name="user-list"),
	path('user-detail/<int:pk>/', userDetail, name="user-detail"),
	path('new-user/', newUser, name="new-user"),
	path('update-user/<int:pk>/', updateUser, name="update-user"),
	path('delete-user/<int:pk>/', deleteUser, name="delete-user"),
	path('material-list/', materialList, name="material-list"),
	path('material-detail/<int:pk>/', materialDetail, name="material-detail"),
	path('material-create/', createMaterial, name="material-create"),
 	path('update-material/<int:pk>/', updateMaterial, name="update-material"),
	path('delete-material/<int:pk>/', deleteMaterial, name="delete-material"),
	path('comment-list/', commentList, name="comment-list"),
	path('comment-detail/', commentDetail, name="comment-detail"),
	path('comment-create/', createComment, name="comment-create"),
 	path('update-comment/<int:pk>/', updateComment, name="update-comment"),
	path('delete-comment/<int:pk>/', deleteComment, name="delete-comment"),
]