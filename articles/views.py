from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from .serializers import UserSerializer,ArticleSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import Article
from rest_framework.decorators import action
from .permissions import IsAuthorOrReadOnly, CanPublishPermission

# Create your views here.
class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ShowArticles(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        elif self.action == 'create':
            return [permissions.IsAuthenticated(), permissions.DjangoModelPermissions()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsAuthorOrReadOnly()]
        return [permissions.IsAuthenticated()]
    
    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Article.objects.filter(is_published=True)
        return Article.objects.all()
    
    @action(detail=True, methods=['post'], permission_classes = [CanPublishPermission])
    def publish(self, request, pk=None):
        article = self.get_object()
        article.is_published = True
        article.save()
        return Response({'status': 'Article was published'})

class Dashboard(generics.ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Article.objects.filter(author = self.request.user)