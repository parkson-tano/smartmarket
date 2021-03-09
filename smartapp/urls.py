from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IndexView.as_view(), name='index'),
    path('register/', CustomerRegisistraionView.as_view(), name='register'),
    # path('oauth/', include('social_django.urls')),

]
