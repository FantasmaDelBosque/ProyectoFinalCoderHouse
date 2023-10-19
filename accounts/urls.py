from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginView, name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('register/', views.register, name='register'),

    path('home_vendedor/', views.home_vendedor, name='home_vendedor'),

    path('agregar_ropa/', views.agregar_ropa, name='agregar_ropa'),
    path('lista-ropa/', views.lista_ropa, name='lista_ropa'),
    path('editar_ropa/<int:ropa_id>/', views.editar_ropa, name='editar_ropa'),
    path('eliminar_ropa/<int:ropa_id>/', views.eliminar_ropa, name='eliminar_ropa'),

]




