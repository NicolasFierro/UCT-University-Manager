from django.contrib import admin
from .models import Register, LoginStudent, LoginAdmins, Careers

# Registrar tus modelos personalizados
admin.site.register(LoginStudent)
admin.site.register(LoginAdmins)
admin.site.register(Register)
admin.site.register(Careers)