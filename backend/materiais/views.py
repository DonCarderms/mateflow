from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
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
			'Update':'/user-update/<str:pk>/',
			'Delete':'/user-delete/<str:pk>/',
		},
		'material': {		
			'List':'/material-list/',
			'Detail View':'/material-detail/<str:pk>/',
			'Create':'/material-create/',
			'Update':'/material-update/<str:pk>/',
			'Delete':'/material-delete/<str:pk>/',
		},
		'comment': {		
			'List':'/comment-list/',
			'Detail View':'/comment-detail/<str:pk>/',
			'Create':'/comment-create/',
			'Update':'/comment-update/<str:pk>/',
			'Delete':'/comment-delete/<str:pk>/',
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
	print(f'json: {request.data}')
	serializer = User(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)