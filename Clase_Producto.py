class Producto(object):
    def __init__(self):
        print"Ingrese los datos del producto."
        self.tipo=raw_input("Ingrese el tipo de articulo:")
        self.cantidad=int(raw_input("Ingrese la cantidad de articulos: "))
        self.costo=int(raw_input("Ingrese el costo del articulo:"))
    def imprimir(self):
        print"-Los datos del producto son:-"
        print"tipo:"+self.tipo
        print"cantidad: "+self.cantidad
        print"costo:"+self.costo
        
        