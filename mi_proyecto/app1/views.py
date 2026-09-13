from django.http import HttpResponse

def inicio_app1(request):
    return HttpResponse("<h1>App 1 - Vista Inicio</h1><p>Esta es la vista principal de la primera app.</p>")

def detalle_app1(request):
    return HttpResponse("<h1>App 1 - Vista Detalle</h1><p>Esta es la segunda vista de la primera app.</p>")