from django import template

register = template.Library()

@register.filter(name='saludo')
def saludo (value):
    largo=''
    if len(value)>=8:
        largo= '<p>Tu nombre es muy largo </p>'
    return f'<h1 style="background:green;color:white;">Bienvenido, {value}</h1>'+largo

@register.filter(name='multiplicar')
def multiplicar(value, factor):
    return value * factor  # Multiplica el valor por el factor

@register.filter(name='reverso')
def reverso(value):
    return value[::-1]     # Revertir el valor (cambiar el orden de los elementos)

@register.filter(name='longitud')
def longitud(value):
    return len(value) # Obtener la longitud del valor (numero de elementos)

@register.filter(name='negrita')
def negrita(value):
    return f'<strong>{value}</strong>' # Colcoar el texto en negrita




