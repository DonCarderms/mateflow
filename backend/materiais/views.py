from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import UserSerializer, MaterialSerializer, CommentSerializer
from .models import Material, User, Comment


class UserV1(viewsets.ModelViewSet):
		serializer_class = UserSerializer
		queryset = User.objects.all()
		ordering_fields = ['id']
		# permission_classes = [IsAccountAdminOrReadOnly]

		def create(self, request):
				serializer = UserSerializer(data=request.data)
				if serializer.is_valid():
					serializer.save()

				return Response(serializer.data)

		def update(self, request, pk):
			user = User.objects.get(id=pk)
			serializer = UserSerializer(instance=user, data=request.data)
			if serializer.is_valid():
				serializer.save()
			return Response(serializer.data)

		def delete(self, request, pk):
			user = User.objects.get(id=pk)
			user.delete()
			return Response("User deletado com sucesso")

		@action(detail=True, url_path='(?P<material_pk>[^/.]+)/materiais', methods=['get'])
		def get_materiais_user(request, pk):
			materiais = Material.objects.filter(user_id=pk)
			serializer = MaterialSerializer(materiais, many=True)
			return Response(serializer.data)

		@action(detail=True, url_path='(?P<comment_pk>[^/.]+)/comments', methods=['get'])
		def get_comments_user(request, pk):
			comments = Comment.objects.filter(user_id=pk)
			serializer = CommentSerializer(comments, many=True)
			return Response(serializer.data)

class MateriaisV1(viewsets.ModelViewSet):
		serializer_class = MaterialSerializer
		queryset = Material.objects.all()
		ordering_fields = ['id']

		def create(self, request):
			serializer = MaterialSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()

			return Response(serializer.data)

		def update(self, request,  pk):
			material = Material.objects.get(id=pk)
			serializer = MaterialSerializer(instance=material, data=request.data)
			if serializer.is_valid():
				serializer.save()
			return Response(serializer.data)

		def delete(request, pk):
			material = Material.objects.get(id=pk)
			material.delete()
			return Response("material deleted successfully")

		@action(detail=True, url_path='(?P<comment_pk>[^/.]+)/comments', methods=['get'])
		def get_comments_material(self, request, pk):
			comments = Comment.objects.filter(material_id=pk)
			serializer = CommentSerializer(comments, many=True)
			return Response(serializer.data)


class CommentsV1(viewsets.ModelViewSet):
		serializer_class = CommentSerializer
		queryset = Comment.objects.all()
		ordering_fields = ['id']

		def create(self, request):
			serializer = CommentSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()

			return Response(serializer.data)

		def update(self, request, pk):
			comment = Comment.objects.get(id=pk)
			serializer = CommentSerializer(instance=comment, data=request.data)
			if serializer.is_valid():
				serializer.save()
			return Response(serializer.data)

		def delete(self, request, pk):
			comment = Comment.objects.get(id=pk)
			comment.delete()
			return Response("commentario deletado ")





