"""Proyecto_Final_de_BIOS_Python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cerveceria.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('contacto/', contacto, name='contacto'),
    path('sobre-nosotros/', sobre_nosotros, name='sobre-nosotros'),
    path('resultados-busqueda/', buscar_cerveza, name='resultados-busqueda'),
    path('productos/', nuestros_productos, name='nuestros-productos'),
    path('product-details/<int:id>', product_details, name='product-details'),
    path('ordenados-por/', productos_ordenados, name='ordenados-por'),
    path('registro/', new_user, name= 'registro'),
    path('ingresar/', ingresar, name='ingresar'),
    path('privado/', privado, name='privado'),
    path('salir/', salir, name ='salir'),
]

handler404 = page_not_found
handler500 = error_500

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
