from django.shortcuts import render_to_response,render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import Context,loader, RequestContext
from .models import *
from .forms import  *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
import json



def home(request):
	dato = "test"
	if request.method == 'POST':
		form = TestForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['typeahead']:
				messages.success(
					request,
					form.cleaned_data['typeahead']
				)
				dato = get_object_or_404(Producto, titulo=form.cleaned_data['typeahead'])
	else:
		form = TestForm()
	usuario=Usuario.objects.all()
	return render(request,"home.html",{"productos": Productos.objects.all(), "usuario":Usuario.objects.all(),'form': form, 'dprod': dato})

def producto(request,idPel):

	precios = ProductoPrecio.objects.all()
	dato = get_object_or_404(Producto, pk=id_producto)
	return render(request,"peliculas.html",{"dprod":dato,"dprecio":precios})

def super(request):
	supermercado = Supermercado.objects.all() #Capturo todos los cines
	return render(request,"cines.html",{'dsuper':supermercado}) 
	#Se usa la platilla indicada y le pasamos un diccionario

def lista_productos(request):
	dato = Productos.objects.all()
	precios = ProductoPrecio.objects.all()
	return render(request,"lista_peliculas.html",{'dprod':dato, 'dprecio':precios})

def catalogo(request,idCine):
	geo = Location.objects.all()
	dato = Productos.objects.all()
	supermercado = get_object_or_404(Supermercado,pk=id_supermercado)
	return render(request,"cartelera_cine.html",{'dsuper':supermercado,'dprod':dato,'dgeo':geo})

def estrellitas(request):
	nota = int(request.POST.get("nota", ""))	
	pelicula= int(request.POST.get("id", ""))
	pelicula_real=get_object_or_404(ProductoPrecio, pk=id_producto_precio)
	dato = get_object_or_404(ProductoPrecio, pk=id_producto_precio)
	if nota==1
		dato.cant_valoracionneg=dato.cant_valoracionneg+1
	else
		dato.cant_valoracionpos=dato.cant_valoracionpos+1
	usuario= request.user
	try:
		num = get_object_or_404(Valoracion, id_usuario=id_usuario,id_producto_precio=id_producto_precio)
	except:
		num = 0
	if (num != 0):
		print ""
	else: 
		rela= Valoracion(id_producto_precio = pelicula_real, id_usuario= usuario, valoracion=nota)	
		dato.save()
		rela.save()
	response_data = {}
	try:
		response_data['result']= 'funciono'
		response_data['nota']=num
	except:
		response_data['result']='we lost'
		response_data['message']='we fuken lost'
	return HttpResponse(json.dumps(response_data),content_type="application/json")


def contacto(request):
	return render(request,"contacto.html")

def perfil(request):
	perfil = Profile.objects.all()	
	usuario=request.user.id
	if request.POST:
		form = PerfilForm(request.POST.copy())
		form.data['id_2']=usuario
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/home')
		else:
			return HttpResponseRedirect('/quienes-somos/')
	else:
		form = PerfilForm()
	return render(request,"perfil.html",{'dperfil':perfil, 'form':form})


