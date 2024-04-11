from django.shortcuts import render, HttpResponse, redirect
from miApp.models import Article
from django.db import connection
from django.db.models import Q
from miApp.forms import FormArticulo,LoginForm,CreateUserForm,ForgotPasswordForm
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import AgregarCareersForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .forms import AgregarMateriaForm
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
layout="""
        <h1>S</h1>
        </hr>
        <ul>
            <li>
                <a href="/holaMundo">Hola Mundo</a>
            </li>

            <li>
                <a href="/saludo">Saludo</a>
            </li>

            <li>
                <a href="/Inicio">Inicio</a>
            </li>

            <li>
                <a href="/presentacion">Presentacion</a>
            </li>

            <li>
                <a href="/contacto">Contacto</a>
            </li>

        </ul>
        """
def holaMundo (request):
    return render (request, 'holaMundo.html')
def saludo (request):
    return render (request,'saludo.html')
def index(request):
    añosPares = []
    añosViciesto= []
    year = 2024
    while year <= 2050:
        if year % 2 == 0:
            añosPares.append(year)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            añosViciesto.append(year)
        year += 1

    even_years_html = "<h2>AÑOS PARES:</h2><ul>"
    for year in añosPares:
        even_years_html += f"<li>{year}</li>"
    even_years_html += "</ul>"

    leap_years_html = "<h2>AÑOS VICIESTOS:</h2><ul>"
    for year in añosViciesto:
        leap_years_html += f"<li>{year}</li>"
    leap_years_html += "</ul>"
    Nombre = 'Sebastian Tovar'
    lenguajes=['JavaScript', 'Python', 'PHP', 'C']

    # Ejemplo de ciclo for para generar una lista de colores
    colores = ["morado", "cafe", "negro", "rosado", "gris"]

    #Ejemplo de ciclo while para generar los numeros imapares
    impares = []
    num = 1
    while num <= 10:
        impares.append(num)
        num += 2

        # Ejemplo de bucle for
    nombres = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    i = 0
    nombres_while = []
    while i < len(nombres):
        nombres_while.append(nombres[i])
        i += 1

        year=2024
        hasta = range(year,2050)


    template = f"""
                    <h1>Inicio</h1>
                    <p>Años pares y años bisiestos desde 2024 hasta 2050:</p>
                    {even_years_html}
                    {leap_years_html}
                """

    return render(request, 'index.html',{
        'mi_variable':'Soy un dato que esta en la vista','title':'Inicio del sitio','titulo':'Pagina Inicio SENA', 'name':Nombre,'colores': colores,'impares': impares, 'nombres_while': nombres_while,'lenguajes':lenguajes, 'years':hasta,
    })



def presentacion (request):
    return render (request, 'presentacion.html')

def contacto(request,nombre="",apellido=""):
    aprendiz =""
    if nombre and apellido:
        aprendiz = "<h2> Nombre completo: </h2>"
        aprendiz += f"<h3> {nombre} {apellido} </h3>"
    elif nombre:
        aprendiz = "<h2>Nombre sin apellido</h2>"
        aprendiz+= f"<h2> Bienvenido {nombre}</h2>"
    elif apellido:
        aprendiz = "<h2>Apellido sin nombre</h2>"
        aprendiz+= f"<h2> Bienvenido {apellido}</h2>"
    else:
        aprendiz = "<h2> Sin nombre y apellidos definidos</h2>"

        contacto="""
            Bienvenido al apartado de contactos :
            """
        
    # return HttpResponse (layout+f"<h2>contacto:</h2> "+aprendiz)
    return render(request,'contacto.html',)

def quienesSomos(request):
    return render(request,'quienesSomos.html')

def productAndServices(request):
    return render(request,'productAndServices.html')

def pagina(request,redirigir = 0):
    if redirigir == 1:
        return redirect('contacto', nombre ="Ana", apellidos = "Perez")
    return render(request,'pagina.html' , {'texto':'Este es mi texto', 'lista':['uno','dos','tres'],})


def crear_articulo(request, title, content, public):
        articulo= Article(
        title=title,
        content=content,
        public= public,
    )
        articulo.save()
        return HttpResponse(f"Articulo Creado: {articulo.title}-{articulo.content}")

def articulo(request):
    try:
        articulo = Article.objects.get(pk=6, public= True)
        response =f"Articulo Consultado: {articulo.title}-{articulo.content} - Estado: {articulo.public}"
    except:
        response= "<strong> Articulo no Encontrado </strong>"

    return HttpResponse(response)


def editar_articulo(resquest):
    articulo = Article.objects.get(pk=6)
    articulo.title ="Las Aventuras de mafalda"
    articulo.public =True
    articulo.save()
    return HttpResponse(f"El articulo {articulo.id} de nombre: {articulo.title} ha sido actualizado y su estado es: {articulo.public}")

def articulos(request):
    articulos = Article.objects.order_by('id')
    # articulos = Article.objects.filter(title = "articulo 4")
    # articulos = Article.objects.filter(public = "True",id=4)
    # articulos = Article.objects.filter(title__contains="articulos")
    # articulos = Article.objects.filter(title__exact="articulos")
    # articulos = Article.objects.filter(title__iexact="rticulos")
    # articulos = Article.objects.filter(title__iexact="articulos 4")
    # articulos = Article.objects.filter(id__gt=1)
    # articulos = Article.objects.filter(id__lte=5)
    # articulos = Article.objects.filter(id__in=[1,2,9,10])
    articulos = Article.objects.filter(
                                title__contains="Art",
                                
                                    ).exclude(
                                        public=True
                                    )
    articulos = Article.objects.order_by('id')
    articulos = Article.objects.filter(
            Q(title__contains = "a")|Q(public = True)
    )
    
    # articulos = Article.objects.raw("SELECT * FROM miApp_article WHERE content like 'L%' AND public = 1")
    
    return render (request,'articulos.html',{
        'articulos': articulos
    })
    return HttpResponse()

def borrar_articulo(request,id):
    articulo= Article.objects.get(pk=id)
    articulo.delete()
    return redirect('Listar')

def eliminar_articulos(request,id):
    Temp= (f"DELETE FROM miApp_article Where id=%s")
    with connection.cursor() as cursor:
        cursor.execute(Temp, [id])
        articulos= Article.objects.all()
    return render(request,'articulos.html',{'articulos':articulos})

def actualizar_articulos(request,title,id):
    Temp =(f"UPDATE miApp_article SET title=%s WHERE id=%s")
    with connection.cursor() as cursor:
        cursor.execute(Temp, [title,id])
        articulos = Article.objects.all()
    return render(request,'articulos.html',{'articulos':articulos})

def save_articulo(request):
    if request.method == 'POST':
        title = request.POST["title"]
        if len(title)<=5:
                return HttpResponse("El titulo del articulo debe ser mayor a 5 caracteres")
        content= request.POST['content']
        public=request.POST['public']
        articulo= Article(
        title=title,
        content=content,
        public= public,
        )
        articulo.save()
        return HttpResponse(f"Articulo Creado: {articulo.title} - {articulo.content} ")
    else:
        return HttpResponse("El articulo no fue creado")

def create_articulo(request):
    return render(request,'create_articulo.html')

def create_full_articulos(request):
    if request.method == 'POST':
        formulario= FormArticulo(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            title = data_form.get('title')
            content = data_form.get('content')
            public = data_form.get('public')

            articulo= Article(
            title=title,
            content=content,
            public= public,
            )
            articulo.save()
        # return HttpResponse(title + ' ' + content + ' ' +str(public))
            messages.success(request, f'El articulo {articulo.id} se ha guardado satisfactoriamente')
            return redirect('Listar')
        else:
            return render(request,'create_full_articulos.html',{'form':formulario})
    else:
        formulario= FormArticulo()
        return render(request,'create_full_articulos.html',{'form':formulario})



def create_user(request):
    form = CreateUserForm()  # Initialize the form variable outside the if statement
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            phone = form.cleaned_data['phone']


            if password == confirm_password:
                # Tu usuario será creado si todos los campos son llenados y tus contraseñas coinciden
                user = User.objects.create_user(username=username, password=password)

                # Aquí podrías agregar lógica adicional si es necesario

                return redirect('dashboard')  # Cambia 'ruta_donde_redirigir' por la URL a la que quieres redirigir después de guardar

            else:
                # Si tu contraseña no coincide te saldra un mensaje de error
                form.add_error('confirm_password', 'Tus contraseñas no coinciden')

    return render(request, 'create_user.html', {'form': form})

def login(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username , password=password)
        
        if user is not None:
            login(request, user)
            return redirect("inicio")
        else:
            messages.warning(request, "Su usuario o contraseña no coinciden")

    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('login')


def create_groups(sender, **kwargs):
    Group.objects.get_or_create(name='student')
    Group.objects.get_or_create(name='teacher')
    Group.objects.get_or_create(name='admin')

def create_user(request):
    form = CreateUserForm()  # Initialize the form variable outside the if statement
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                # Tu usuario sera creado si todos los campos son llenados y tus contraseñas coinciden
                user = User.objects.create_user(username=username, password=password)
                # Here you could add additional logic
            else:
                # Si tu contraseña no coincide te saldra un mensaje de error
                form.add_error('confirm_password', 'Tus contraseñas no coincide')
    return render(request, 'create_user.html', {'form': form})

def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            # Esta opcion envia un correo electrónico para restablecer la contraseña
            pass
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgot_password.html', {'form': form})

def dashboard(request):
    materias = Careers.objects.filter(profesor=request.user)
    form = AgregarMateriaForm()
    if request.method == 'POST':
        form = AgregarMateriaForm(request.POST)
        if form.is_valid():
            Careers = form.save(commit=False)
            Careers.profesor = request.user
            Careers.save()
            return redirect('dashboard')
    return render(request, 'dashboard.html', {'materias': materias, 'form': form})

def eliminar_materia(request, id_materia):
    Careers = Careers.objects.get(id=id_materia)
    if request.user == Careers.profesor:
        Careers.delete()
    return redirect('dashboard')

def agregar_materia(request):
    if request.method == 'POST':
        form = AgregarMateriaForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige al usuario a la página de éxito o a donde quieras
            return redirect('dashboard')
    else:
        form = AgregarMateriaForm()
    
    return render(request, 'agregar_materia.html', {'form': form})

def agregar_carrera(request):
    if request.method == 'POST':
        form = AgregarCareersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AgregarCareersForm()
    return render(request, 'agregar_carrera.html', {'form': form})

from django.shortcuts import render

def ingenieria_informatica(request):
    return render(request, 'ingenieria_informatica.html')

def administracion_empresas(request):
    return render(request, 'administracion_empresas.html')

def psicologia(request):
    return render(request, 'psicologia.html')

def medicina(request):
    return render(request, 'medicina.html')

def derecho(request):
    return render(request, 'derecho.html')

def arquitectura(request):
    return render(request, 'arquitectura.html')

def contaduria_publica(request):
    return render(request, 'contaduria_publica.html')

def enfermeria(request):
    return render(request, 'enfermeria.html')

def is_student(user):
    return user.is_authenticated and hasattr(user, 'loginstudent')

def is_professor(user):
    return user.is_authenticated and hasattr(user, 'profesor')

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'loginadmins')

@login_required
@user_passes_test(is_student)
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@login_required
@user_passes_test(is_professor)
def professor_dashboard(request):
    return render(request, 'professor_dashboard.html')

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

