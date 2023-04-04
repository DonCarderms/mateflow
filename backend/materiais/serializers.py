from rest_framework import serializers
from .models import Material, User, Comment

class MaterialSerializer(serializers.ModelSerializer):
	class Meta:
		model = Material
		fields ='__all__'
  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
        