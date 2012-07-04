#coding: utf-8
from Garantia_Prendaria import GarantiaPrendaria
from Tarjeta_De_Circulacion import TarjetaDeCirculacion

class VehiculosYMaquinaria(GarantiaPrendaria):
    def __init__(self):
        GarantiaPrendaria.__init__(self,36)
        self.tarjetaDeCirculacion=TarjetaDeCirculacion()
    def imprimir(self):
        GarantiaPrendaria.imprimir(self)
        self.tarjetaDeCirculacion.imprimir()
        print"Cuota es de: Q.%f0.2"%(self.cuota)
    def calcular(self):
        self.cuota=self.monto*(0.015/(1-(1+0.015)**((self.cuotas)*-1)))
    def Guardar(self):
        try:
            archivo=open("Archivos/VehiculosYMaquinaria.txt","a")
        except:
            archivo=open("Archivos/VehiculosYMaquinaria.txt","w")
        archivo.write(self.cliente.nombre+" "+self.cliente.segudnonombre+" "+self.cliente.primerapellido+" "+self.cliente.segundoapellido+" "+self.cliente.dirreccioncliente+" "+self.cliente.correocliente+" "+str(self.cliente.telfonocliente)+" "+str(self.tarjetaDeCirculacion.numero)+" "+str(self.tarjetaDeCirculacion.fechaDeEmision)+" "+str(self.tarjetaDeCirculacion.fechaDeCaducidad)+" "+str(self.monto)+" "+str(self.cuotas)+" "+str(self.cuota)+" "+self.nocredito+"¬")
        archivo.close()
    
        