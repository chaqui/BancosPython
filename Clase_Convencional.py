from Garantia_Prendaria import GarantiaPrendaria
from produccion import Producto
class Convencional(GarantiaPrendaria):
    def __init__(self):
        GarantiaPrendaria.__init__(self)
        self.producto=Producto()
    def calcular(self):
        self.cuota=self.monto*(0.01667/(1-(1+0.01667)**((self.cuotas)*-1)))
    def imprimir(self):
        GarantiaPrendaria.imprimir(self)
        self.producto.imprimir()
        print"las cuota es: "+self.cuota
    def guardar(self):
        try:
            archivo=open("Archivos/Clase_Convencional.txt","a")
        except:
            archivo=open("Archivos/Clase_Convencional.txt","w")
        archivo.write(self.cliente.nombre+" "+self.cliente.segudnonombre+" "+self.cliente.primerapellido+" "+self.cliente.segundoapellido+" "+self.cliente.dirreccioncliente+" "+self.cliente.correocliente+" "+str(self.cliente.telfonocliente)+" "+str(self.monto)+" "+str(self.cuotas)+" "+str(self.cuota)+" "+str(self.libro)+" "+str(self.finca)+" "+str(self.folio)+" "+str(self.registroDeInscripcion)+"¬")
        archivo.close()
        
        
        
        