from django.contrib import admin

# Register your models here.


from CineAltiro.models import *
admin.site.register(Producto)
admin.site.register(ProductoPrecio) 
admin.site.register(Reporte) 
admin.site.register(Supermercado)
admin.site.register(Usuario)
admin.site.register(Valoracion)

class UsuarioAdmin(admin.ModelAdmin):

	list_display = ('nombre,nick,status')


class ShowTimeAdmin(admin.ModelAdmin):
	fields = ['cines','peliculas','horarios','tipo','date']
	list_display = ('cines','peliculas','tipo','date')

admin.site.register(ShowTime,ShowTimeAdmin) 



