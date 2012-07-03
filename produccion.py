

class Producto(object):
    def __init__(self):
        print "ingrese los datos del producto"
        self.tipo=raw_input("Ingrese el tipo de producto:")
        self.cantidad=raw_input("Porfavor ingrese la cantidad de produccion:")
        self.costo=raw_input("Ingrese el valor de produccion:")
    def imprimir(self):
        print"-Datos del Producto-"
        print"tipo de producto:"+self.tipo
        print"cantidad de produccion"+str(self.cantidad)
        print"valor de produccioN: "+str(self.costo)        
        