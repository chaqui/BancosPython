#coding: utf-8
from Credito import Credito
from fiduciario import Fiduciario
class CreditoFiduciario(Credito):
    def __init__(self,maximo):
        Credito.__init__(self,maximo)
        print("datos del fiduciario")
        self.fiduciario1=Fiduciario()
    def imprimir(self):
        Credito.imprimir(self)
        self.fiduciario1.imprimir()
        
    
    
          
        