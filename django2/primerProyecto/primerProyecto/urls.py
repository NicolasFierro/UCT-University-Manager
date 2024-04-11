"""
URL configuration for primerProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from miApp import views
from django.conf import settings
import miApp.views 

urlpatterns = [
    path('admin/', admin.site.urls),  # para acceder al administrador de Django
    path('holaMundo/', views.holaMundo, name="Hola Mundo"), #Cuando se llama a esta vista se ejecutara la funcion holaMundo
    path('saludo/',views.saludo, name="Saludo"), 
    path('Inicio',views.index, name="Index"),
    path('presentacion/',views.presentacion, name="Presentacion"),
    # path('contacto/',miApp.views.contacto, name="Contacto"),
    # path('contacto/<str:nombre>',miApp.views.contacto, name="Contacto"),
    # path('contacto/<str:nombre>/<str:apellido>',miApp.views.contacto, name="Contacto"),
    path('quienesSomos/',views.quienesSomos, name="QuienesSomos"),
    path('productAndServices/',miApp.views.productAndServices, name="Productos  y Servicios"),
    path('contacto/',miApp.views.contacto, name="contacto"),
    path('', views.index, name='Inicio'),
    path('pagina/',miApp.views.pagina, name="Pagina"),
    path('crear_articulo/', miApp.views.crear_articulo, name="crear articulo"),
    path('crear_articulo/<str:title>/<str:content>/<str:public>', miApp.views.crear_articulo, name="crear articulo"),
    path('articulo/', miApp.views.articulo, name="Articulo"),
    path('editar_articulo/', miApp.views.editar_articulo, name="editar_articulo"),
    path('articulos/', miApp.views.articulos, name="Listar"),
    path('borrar_articulo/<int:id>', miApp.views.borrar_articulo, name="Borrar"),
    path('eliminar_articulos/<int:id>', miApp.views.eliminar_articulos, name='eliminar'),
    path('actualizar_articulos/<str:title>/<int:id>',miApp.views.actualizar_articulos, name='actualizar'),
    path('create_articulo/',miApp.views.create_articulo, name='Crear'),
    path('create_articulo/',miApp.views.save_articulo, name='Guardar'),
    path('create-full-articulos/',miApp.views.create_full_articulos, name='Create Full Article'),
    path('login/', miApp.views.login, name='login'),
    path('dashboard/', miApp.views.dashboard, name='dashboard'),
    path('agregar_carrera/', miApp.views.agregar_carrera, name='agregar_carrera'),
    path('materia/agregar/', miApp.views.agregar_materia, name='agregar_materia'),
    path('eliminar_materia/<int:id_materia>/', miApp.views.eliminar_materia, name='eliminar_materia'),
    path('create_user/', miApp.views.create_user, name='create_user'),
    path('forgot_password/', miApp.views.forgot_password, name='forgot_password'),
    path('login/forgot_password/', miApp.views.forgot_password, name='forgot_password'),
    path('ingenieria_informatica/', views.ingenieria_informatica, name='ingenieria_informatica'),
    path('administracion_empresas/', views.administracion_empresas, name='administracion_empresas'),
    path('psicologia/', views.psicologia, name='psicologia'),
    path('medicina/', views.medicina, name='medicina'),
    path('derecho/', views.derecho, name='derecho'),
    path('arquitectura/', views.arquitectura, name='arquitectura'),
    path('contaduria_publica/', views.contaduria_publica, name='contaduria_publica'),
    path('enfermeria/', views.enfermeria, name='enfermeria'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
