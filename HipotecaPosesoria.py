#coding: utf-8
from Hipotecari import Hipoteca
class HipotecaPosesoria(Hipoteca):



    def __init__(self):
        Hipoteca.__init__(self)
        self.escritura=int(raw_input("Ingrese el numero de escritura del documento:"))
        self.nombremunicipalidad=raw_input("Ingrese el nombre de la municipalidad:")
    def calcular(self):
        self.cuota=self.monto*(0.015/(1-(1+0.015)**((self.cuotas)*-1)))
    def imprimir(self):
        Hipoteca.imprimir(self)
        print "numero de escritura:"+str(self.escritura)+"nombre de la muncipalidad:"+self.nombremunicipalidad
        print "las cuota es de: Q.%0.2f "%(self.cuota)
    def guardar(self):
        try:
            archivo=open("Archivos/HipotecaPosesoria.txt","a")
        except:
            archivo=open("Archivos/HipotecaPosesoria.txt","w")
        archivo.write(self.cliente.nombre+" "+self.cliente.segudnonombre+" "+self.cliente.primerapellido+" "+self.cliente.segundoapellido+" "+self.cliente.dirreccioncliente+" "+self.cliente.correocliente+" "+str(self.cliente.telfonocliente)+" "+str(self.monto)+" "+str(self.cuotas)+" "+str(self.cuota)+" "+str(self.libro)+" "+str(self.finca)+" "+str(self.folio)+" "+str(self.escritura)+self.nombremunicipalidad+"¬")
        archivo.close()
        
        
        
        
        