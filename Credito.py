#coding: utf-8
from Cliente import Cliente1
class Credito(object):
    '''
    classdocs
    '''
    

    def __init__(self,maxima):
        print("ingrese los datos del cliente")
        self.cliente=Cliente1()
        self.cliente.ingresar()
        print"ingrese los datos del credito"
        self.monto=float(raw_input("ingrese el monto del credito:"))
        self.cuotas=1
        while((self.cuota>=maxima)or(self.cuotas<1)):
            self.cuotas=int(raw_input("cuotas:"))
            if ((self.cuota>=maxima)or(self.cuota<1)):
                print"error numero incorrecto"             
        self.nocredito=1
    def imprimir(self):
        
        self.cliente.imprimir()
        a="/"*80
        print a
        print "datos del Credito"
        print"No. de credito:"+str(self.nocredito)
        print("monto: "+str(self.monto)+"\n Cuotas:"+str(self.cuotas))
