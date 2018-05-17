from django.urls import path, include

from . import views

app_name = 'users-login'

urlpatterns = [
	path('', include('django.contrib.auth.urls')),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
]