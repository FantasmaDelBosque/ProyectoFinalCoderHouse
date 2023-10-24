from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm # Usa el formulario de usuario predeterminado
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import UserEditForm, AvatarForm, RopaForm, ZapatosForm, AccesoriosForm
from .models import Ropa, Zapatos, Accesorios, Avatar







def home(request):

    return render(request, "home.html")


def home_vendedor (request):

    return render(request, "home_vendedor.html")

def sobre_mi (request):

    return render(request, "sobre_mi.html")



@login_required
def profile(request):
    user_avatar = None
    if request.user.is_authenticated:
        try:
            user_avatar = Avatar.objects.get(user=request.user)# pylint: disable=no-member
        except Avatar.DoesNotExist:# pylint: disable=no-member
            pass

    return render(request, 'profile.html', {'user_avatar': user_avatar})



def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "home_vendedor.html", {"mensaje": f"Bienvenidx {username}!"})
            else:
                return render(request, "home.html", {"mensaje": "Datos incorrectos"})
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logoutView(request):
    logout(request)
    # No necesitas mensajes aquí
    return redirect('home')




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')
        else:
            messages.error(request, 'Error en el registro. Por favor, asegúrate de que las contraseñas coincidan.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})




@login_required
def edit_user_profile(request):

    usuario = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=usuario)

        if form.is_valid():

            data = form.cleaned_data
            usuario.username = data["username"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render(request, "profile.html", {"mensaje": "Datos actualizados con éxito!"})
        else:
            return render(request, "edit_profile.html", {"form": form})
    else:
        form = UserEditForm(instance=usuario)
        return render(request, "edit_profile.html", {"form": form})
    





@login_required
def agregar_ropa(request):

    if request.method == 'POST':
        form = RopaForm(request.POST, request.FILES)
        if form.is_valid():
            ropa = form.save(commit=False)
            ropa.usuario = request.user  # Asigna el usuario actual
            ropa.save()
            return redirect('lista_ropa')
    else:
        form = RopaForm()
    
    return render(request, 'agregar_ropa.html', {'form': form})

def lista_ropa(request):

    elementos_ropa = Ropa.objects.all()# pylint: disable=no-member
    return render(request, 'lista_ropa.html', {'ropa': elementos_ropa})

@login_required
def editar_ropa(request, ropa_id):

    ropa = Ropa.objects.get(pk=ropa_id)# pylint: disable=no-member

    if ropa.usuario == request.user:
        if request.method == 'POST':
            form = RopaForm(request.POST, request.FILES, instance=ropa)
            if form.is_valid():
                ropa = form.save(commit=False)
                ropa.usuario = request.user
                ropa.save()
                return redirect('lista_ropa')
            
        else:
            form = RopaForm(instance=ropa)
                # Agrega los prints de depuración aquí
        print("Formulario válido:", form.is_valid())
      
     

        return render(request, 'editar_ropa.html', {'form': form, 'ropa': ropa})
    else:
        return HttpResponseForbidden("No tienes permiso para editar esta ropa.")

@login_required
def eliminar_ropa(request, ropa_id):
    ropa = Ropa.objects.get(pk=ropa_id)# pylint: disable=no-member

    if ropa.usuario == request.user:
        ropa.delete()
        return redirect('lista_ropa')
    else:
        return HttpResponseForbidden("No tienes permiso para eliminar esta ropa.")
    
@login_required
def agregar_zapatos(request):
    if request.method == 'POST':
        form = ZapatosForm(request.POST, request.FILES)
        if form.is_valid():
            zapatos = form.save(commit=False)
            zapatos.usuario = request.user  # Establecer el usuario actual
            zapatos.save()
            return redirect('lista_zapatos')

    else:
        form = ZapatosForm()

    return render(request, 'agregar_zapatos.html', {'form': form})


def lista_zapatos(request):
    zapatos = Zapatos.objects.all()# pylint: disable=no-member
    return render(request, 'lista_zapatos.html', {'zapatos': zapatos})

@login_required
def editar_zapatos(request, zapatos_id):
    zapatos = Zapatos.objects.get(pk=zapatos_id) # pylint: disable=no-member

    if zapatos.usuario == request.user:
        if request.method == 'POST':
            form = ZapatosForm(request.POST, request.FILES, instance=zapatos)
            if form.is_valid():
                zapatos = form.save(commit=False)
                zapatos.usuario = request.user
                zapatos.save()
                return redirect('lista_zapatos')

        else:
            form = ZapatosForm(instance=zapatos)
        
        print("Formulario válido:", form.is_valid())

        return render(request, 'editar_zapatos.html', {'form': form, 'zapatos': zapatos})
    else:
        return HttpResponseForbidden("No tienes permiso para editar estos zapatos.")

@login_required
def eliminar_zapatos(request, zapatos_id):
    zapatos = Zapatos.objects.get(pk=zapatos_id)# pylint: disable=no-member  

    if zapatos.usuario == request.user:
        zapatos.delete()
        return redirect('lista_zapatos')
    else:
        return HttpResponseForbidden("No tienes permiso para eliminar estos zapatos.")
    




    
@login_required
def agregar_accesorios(request):
    if request.method == 'POST':
        form = AccesoriosForm(request.POST, request.FILES)
        if form.is_valid():
            accesorios = form.save(commit=False)
            accesorios.usuario = request.user  # Asigna el usuario actual
            accesorios.save()
            return redirect('lista_accesorios') 
    else:
        form = AccesoriosForm()
    
    return render(request, 'agregar_accesorios.html', {'form': form})


def lista_accesorios(request):
    accesorios = Accesorios.objects.all()# pylint: disable=no-member
    return render(request, 'lista_accesorios.html', {'accesorios': accesorios})

@login_required
def editar_accesorios(request, accesorios_id):
    accesorios = Accesorios.objects.get(pk=accesorios_id)# pylint: disable=no-member

    if accesorios.usuario == request.user:
        if request.method == 'POST':
            form = AccesoriosForm(request.POST, request.FILES, instance=accesorios)
            if form.is_valid():
                accesorios = form.save(commit=False)
                accesorios.usuario = request.user
                accesorios.save()
                return redirect('lista_accesorios')

        else:
            form = AccesoriosForm(instance=accesorios)

        print("Formulario válido:", form.is_valid())

        return render(request, 'editar_accesorios.html', {'form': form, 'accesorios': accesorios})
    else:
        return HttpResponseForbidden("No tienes permiso para editar estos accesorios.")

@login_required
def eliminar_accesorios(request, accesorios_id):
    accesorios = Accesorios.objects.get(pk=accesorios_id)# pylint: disable=no-member

    if accesorios.usuario == request.user:
        accesorios.delete()
        return redirect('lista_accesorios')
    else:
        return HttpResponseForbidden("No tienes permiso para eliminar estos accesorios.")
    





@login_required
def agregar_avatar(request):
    try:
        user_avatar = Avatar.objects.get(user=request.user)# pylint: disable=no-member
    except ObjectDoesNotExist:
        user_avatar = None

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if user_avatar:
                # Si el usuario ya tiene un avatar, elimina el avatar existente
                user_avatar.delete()

            avatar = Avatar(user=request.user, imagen=data["imagen"])
            avatar.save()
            return redirect('profile')

    else:
        form = AvatarForm()

    return render(request, "agregar_avatar.html", {"form": form, "user_avatar": user_avatar})




