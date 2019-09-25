from django.shortcuts import render

# Create your views here.
def index(request):
    nombre = "VW Jetta"
    modelo = 2018
    precio = 153000
    color = "Gris"

    dict = { 'auto_nombre' :  nombre , 'auto_modelo' : modelo , 'auto_precio' : precio , 'auto_color' : color
 
    }
    
    return render( request, 'index.html', dict)

