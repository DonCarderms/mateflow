from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .serializers import UserSerializer, MaterialSerializer, CommentSerializer
from .models import Material, User, Comment
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'user': {		
			'List':'/user-list/',
			'Detail View':'/user-detail/<str:pk>/',
			'Create':'/new-user/',
			'Update':'/update-user/<str:pk>/',
			'Delete':'/delete-user/<str:pk>/',
		},
		'material': {		
			'List':'/material-list/',
			'Detail View':'/material-detail/<str:pk>/',
			'Create':'/material-create/',
			'Update':'/update-material/<str:pk>/',
			'Delete':'/delete-material/<str:pk>/',
		},
		'comment': {		
			'List':'/comment-list/',
			'Detail View':'/comment-detail/<str:pk>/',
			'Create':'/comment-create/',
			'Update':'/update-comment/<str:pk>/',
			'Delete':'/delete-comment/<str:pk>/',
		},
		}

	return Response(api_urls)



@api_view(['GET'])
def userList(request):
	users = User.objects.all().order_by('-id')
	serializer = UserSerializer(users,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
	user = User.objects.get(id=pk)
	serializer = UserSerializer(user, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def newUser(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response("User deleted successfully")




@api_view(['GET'])
def materialList(request):
	materiais = Material.objects.all().order_by('-id')
	serializer = MaterialSerializer(materiais,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def materialDetail(request, pk):
	material = Material.objects.get(id=pk)
	serializer = MaterialSerializer(material, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def createMaterial(request):
	serializer = MaterialSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def updateMaterial(request, pk):
    material = Material.objects.get(id=pk)
    serializer = MaterialSerializer(instance=material, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteMaterial(request, pk):
    material = Material.objects.get(id=pk)
    material.delete()
    return Response("material deleted successfully")




@api_view(['GET'])
def commentList(request):
	comments = Comment.objects.all().order_by('-id')
	serializer = CommentSerializer(comments,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def commentDetail(request, pk):
	comment = Comment.objects.get(id=pk)
	serializer = CommentSerializer(comment, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def createComment(request):
	serializer = CommentSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def updateComment(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(instance=comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return Response("comment deleted successfully")