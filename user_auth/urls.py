from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
  #  path('login/',views.login, name='login')
]
