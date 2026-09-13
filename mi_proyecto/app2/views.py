from django.http import HttpResponse

def inicio_app2(request):
    return HttpResponse("<h1>App 2 - Vista Inicio</h1><p>Bienvenido a la segunda aplicación.</p>")

def contacto_app2(request):
    return HttpResponse("<h1>App 2 - Vista Contacto</h1><p>Formulario o información de contacto.</p>")