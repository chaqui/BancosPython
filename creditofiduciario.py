'''
Created on 27/06/2012

@author: josuechaqui
'''
from Credito import Credito
from fiduciario import Fiduciario
class CreditoFiduciario(Credito):
    def __init__(self):
        Credito.__init__(self)
        print("datos del fiduciario")
        self.fiduciario1=Fiduciario()
    
    
          
        