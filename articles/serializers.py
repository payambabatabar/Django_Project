from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password': {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
     
    class Meta:
        model = Article
        fields = '__all__'