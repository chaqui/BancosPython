#coding: utf-8
from Hipotecari import Hipoteca
class HipotecaReal(Hipoteca):
    def __init__(self):
        Hipoteca.__init__(self)
        self.registroDeInscripcion=int(raw_input("Ingrese el registro de inscripción del documento:"))
    def calcular(self):
        self.cuota=self.monto*(0.015/(1-(1+0.015)**((self.cuotas)*-1)))
    def imprimir(self):
        Hipoteca.imprimir(self)
        print "las cuota es de: Q.%0.2f "%(self.cuota)
    def guardar(self):
        try:
            archivo=open("Archivos/HipotecaReal.txt","a")
        except:
            archivo=open("Archivos/HipotecaReal.txt","w")
        archivo.write(self.cliente.nombre+" "+self.cliente.segudnonombre+" "+self.cliente.primerapellido+" "+self.cliente.segundoapellido+" "+self.cliente.dirreccioncliente+" "+self.cliente.correocliente+" "+str(self.cliente.telfonocliente)+" "+str(self.monto)+" "+str(self.cuotas)+" "+str(self.cuota)+" "+str(self.libro)+" "+str(self.finca)+" "+str(self.folio)+" "+str(self.registroDeInscripcion)+"¬")
        archivo.close()
hipotecareal=HipotecaReal()
hipotecareal.calcular()
hipotecareal.imprimir()
hipotecareal.guardar()
    
        
        