from django.shortcuts import render

# Create your views here.
def index(request):

    return render( request, 'index.html', {'autos' : autos})

class Auto:
    def __init__ (self, nombre, modelo , precio , color, img_url):
        self.nombre = nombre
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.img_url = img_url

default_image ="https://tiaecuador.vteximg.com.br/arquivos/ids/160501-1000-1000/192156000.jpg" 
autos = [ 
    Auto("VW Jetta", 2018 , 125000 , "Gris", default_image), 
    Auto("Lexus", 2018 , 256000 , "Rojo", default_image ), 
    Auto("Futura", 1954 , 0 , "Aqua", default_image ), 
    Auto("Porsche", 2010 , 250000 , "Azul", default_image ) ,
    Auto("VW GOL", 2018 , 175000 , "Azul", default_image ),
]   