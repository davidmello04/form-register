from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar_usu/', views.cadastrar_usu, name='cadastrar_usu'),
    path('login_user/', views.login_user, name='login_user')
]