from django.contrib import admin
from django.urls import path, include
from articles.views import ShowArticles
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = DefaultRouter()
router.register('articles', ShowArticles)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token', TokenObtainPairView.as_view(), name = 'toke_obtain_pair_view'),
    path('token/refresh', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name = 'token_verify'),
    path('', include('articles.urls'))
]
urlpatterns+=router.urls