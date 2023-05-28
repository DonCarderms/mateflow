from rest_framework import serializers
from .models import Material, Comment, User


class MaterialSerializer(serializers.ModelSerializer):
        class Meta:
            model = Material
            fields = '__all__'
            ordering = ['id']

        def to_representation(self, instance):
            data =  super().to_representation(instance)
            data['created_at'] = f"{instance.created_at.strftime('%d-%m-%Y : %H:%M')}"
            data['updated_at'] = f"{instance.updated_at.strftime('%d-%m-%Y : %H:%M')}"
            return data

class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = [
                'id',
                'last_login',
                'date_joined',
                'is_superuser',
                'username',
                'first_name',
                'last_name',
                'is_staff',
                'is_active',
                'email',
            ]
            ordering = ['id']

        def to_representation(self, instance):
            data =  super().to_representation(instance)
            data['last_login'] = f"{instance.last_login.strftime('%d-%m-%Y : %H:%M')}"
            data['date_joined'] = f"{instance.last_login.strftime('%d-%m-%Y : %H:%M')}"
            return data

class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'
            ordering = ['id']

        def to_representation(self, instance):
            data =  super().to_representation(instance)
            data['created_at'] = f"{instance.created_at.strftime('%d-%m-%Y : %H:%M')}"
            data['updated_at'] = f"{instance.updated_at.strftime('%d-%m-%Y : %H:%M')}"
            return data