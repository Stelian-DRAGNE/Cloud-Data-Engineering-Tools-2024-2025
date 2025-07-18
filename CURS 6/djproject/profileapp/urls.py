from django.urls import path, include
from .views import profile_view, only_logged_users_view

urlpatterns = [
    path('profile/', profile_view, name='profile_url'),
    path('doarlogat/', only_logged_users_view),
]