from django.urls import path
from . import views

app_name= 'auth'

urlpatterns = [
   path('login/', views.user_login, name='login'),
   path('register/', views.signup, name='register'),
   path('logout/', views.user_logout, name='logout'),
   # path('forgot-password/', views.user_forgot_password, name='forgot-password'),
   # path('reset-password/<str:token>/', views.user_reset_password, name='reset-password'),
]