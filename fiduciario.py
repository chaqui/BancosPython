'''
Created on 27/06/2012

@author: josuechaqui
'''
from Cliente import Cliente1
class Fiduciario(Cliente1):
    
    def __init__(self):
        pass
    def imprimir(self):
        a="/"*80
        print a
        print "datos del fiduciario:"
        print("el usuario es: "+self.nombre+" "+self.segudnonombre+" "+self.primerapellido+" "+self.primerapellido+" "+self.segundoapellido+"\n correo:"+self.correocliente+" \n telefono:"+str(self.telfonocliente)+"\n dirreccion:"+self.dirreccioncliente)