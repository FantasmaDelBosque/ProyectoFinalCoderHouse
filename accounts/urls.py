from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views



urlpatterns = [
    path('home/', views.home, name="home"),
    path('login/', views.loginView, name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('register/', views.register, name='register'),

    path('profile/', views.profile, name='profile'),  
    path('edit_profile/', views.edit_user_profile, name='edit_profile'),
    path('home_vendedor/', views.home_vendedor, name='home_vendedor'),
    path('agregar_avatar', views.agregar_avatar, name='agregar_avatar'),

    path('agregar_ropa/', views.agregar_ropa, name='agregar_ropa'),
    path('lista-ropa/', views.lista_ropa, name='lista_ropa'),
    path('editar_ropa/<int:ropa_id>/', views.editar_ropa, name='editar_ropa'),
    path('eliminar_ropa/<int:ropa_id>/', views.eliminar_ropa, name='eliminar_ropa'),

    path('agregar_zapatos/', views.agregar_zapatos, name='agregar_zapatos'),
    path('lista-zapatos/', views.lista_zapatos, name='lista_zapatos'),
    path('editar_zapatos/<int:zapatos_id>/', views.editar_zapatos, name='editar_zapatos'),
    path('eliminar_zapatos/<int:zapatos_id>/', views.eliminar_zapatos, name='eliminar_zapatos'),

    path('agregar_accesorios/', views.agregar_accesorios, name='agregar_accesorios'),
    path('lista-accesorios/', views.lista_accesorios, name='lista_accesorios'),
    path('editar_accesorios/<int:accesorios_id>/', views.editar_accesorios, name='editar_accesorios'),
    path('eliminar_accesorios/<int:accesorios_id>/', views.eliminar_accesorios, name='eliminar_accesorios'),

]




