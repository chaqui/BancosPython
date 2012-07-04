#coding: utf-8
from Garantia_Prendaria import GarantiaPrendaria
from Clase_Producto import Producto
class NoConvencional(GarantiaPrendaria):
    def __init__(self):
        GarantiaPrendaria.__init__(self,12)
        self.producto=Producto()
    def calcular(self):
        self.cuota=self.monto*(0.01667/(1-(1+0.01667)**((self.cuotas)*-1)))
    def imprimir(self):
        GarantiaPrendaria.imprimir(self)
        self.producto.imprimir()
        print"las cuota es: "+self.cuota
    def guardar(self):
        try:
            archivo=open("Archivos/Clase_No_Convencional.txt","a")
        except:
            archivo=open("Archivos/Clase_No_Convencional.txt","w")
        archivo.write(self.cliente.nombre+" "+self.cliente.segudnonombre+" "+self.cliente.primerapellido+" "+self.cliente.segundoapellido+" "+self.cliente.dirreccioncliente+" "+self.cliente.correocliente+" "+str(self.cliente.telfonocliente)+" "+str(self.monto)+" "+str(self.cuotas)+" "+str(self.cuota)+str(self.producto.tipo)+" "+str(self.producto.cantidad)+" "+str(self.producto.costo)+"¬")
        archivo.close()
        
        
        