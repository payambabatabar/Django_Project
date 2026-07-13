from django.urls import path
from .views import SignupView, Dashboard

urlpatterns = [
    path('signup/', SignupView.as_view(), name = 'signup'),
    path('dashboard/', Dashboard.as_view(), name = 'dashboard')
]
