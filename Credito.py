#coding: utf-8
from Cliente import Cliente1
class Credito(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        print("ingrese los datos del cliente")
        self.cliente=Cliente1()
        self.cliente.ingresar()
        print"ingrese los datos del credito"
        self.monto=float(raw_input("ingrese el monto del credito:"))
        self.cuotas=int(raw_input("cuotas:"))
    def imprimir(self):
        
        self.cliente.imprimir()
        a="/"*80
        print a
        print "datos del Credito"
        print("monto: "+str(self.monto)+"\n Cuotas:"+str(self.cuotas))
