from django.shortcuts import render

# Create your views here.
def index(request):

    return render( request, 'index.html', {'autos' : autos})

class Auto:
    def __init__ (self, nombre, modelo , precio , color):
        self.nombre = nombre
        self.modelo = modelo
        self.precio = precio
        self.color = color

autos = [ 
    Auto("VW Jetta", 2018 , 125000 , "Gris"),
    Auto("Lexus", 2018 , 256000 , "Rojo"),
    Auto("Futura", 1954 , 0 , "Aqua"),
    Auto("Porsche", 2010 , 250000 , "Azul"),
    Auto("VW GOL", 2018 , 175000 , "Azul")

]