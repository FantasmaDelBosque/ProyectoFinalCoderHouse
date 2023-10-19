from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # Usa el formulario de usuario predeterminado
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import RopaForm
from .models import Ropa 


def home(request):
    return render(request, "home.html")

def home_vendedor (request):
    return render(request, "home_vendedor.html")



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

            # Agregar un mensaje de registro exitoso
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')

            return redirect('login')
        else:
            # Agregar un mensaje de error en caso de contraseñas no coincidentes
            messages.error(request, 'Error en el registro. Por favor, asegúrate de que las contraseñas coincidan.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})




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
