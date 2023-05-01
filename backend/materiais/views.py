from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .serializers import UserSerializer, MaterialSerializer, CommentSerializer
from .models import Material, User, Comment


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'user': {		
			'List':'/user-list/',
			'Detail View':'/user-detail/<int:pk>/',
			'Create':'/new-user/',
			'Update':'/update-user/<int:pk>/',
			'Delete':'/delete-user/<int:pk>/',
			'materiais':'/user/<int:pk>/materiais',
			'comments':'/user/<int:pk>/comments',
		},
		'material': {		
			'List':'/material-list/',
			'Detail View':'/material-detail/<int:pk>/',
			'Create':'/material-create/',
			'Update':'/update-material/<int:pk>/',
			'Delete':'/delete-material/<int:pk>/',
			'comments' : '/material/<int:pk>/comments',
		},
		'comment': {		
			'List':'/comment-list/',
			'Detail View':'/comment-detail/<int:pk>/',
			'Create':'/comment-create/',
			'Update':'/update-comment/<int:pk>/',
			'Delete':'/delete-comment/<int:pk>/',
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
    try:
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response("User não existe")

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
    return Response("User deletado com sucesso")

@api_view(['GET'])
def getMateriaisUser(request, pk):
	materiais = Material.objects.filter(user_id=pk)
	serializer = MaterialSerializer(materiais, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def getCommentsUser(request, pk):
	comments = Comment.objects.filter(user_id=pk)
	serializer = CommentSerializer(comments, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def materialList(request):
	materiais = Material.objects.all().order_by('-id')
	serializer = MaterialSerializer(materiais,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def materialDetail(request, pk):
	try:
		material = Material.objects.get(id=pk)
		serializer = MaterialSerializer(material, many=False)
		return Response(serializer.data)
	except Material.DoesNotExist:
		return Response("material não existe ou foi deletado")

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
def getComemntsMaterial(request, pk):
	comments = Comment.objects.filter(material_id=pk)
	serializer = CommentSerializer(comments, many=True)
	return Response(serializer.data)



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
    return Response("commentario deletado ")





