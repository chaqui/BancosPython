'''
Created on 3/07/2012

@author: josuechaqui
'''
from Credito import Credito
class GarantiaPrendaria(Credito):
    def __init__(self,maximo):
        Credito.__init__(self,maximo)
        print ("datos del producto:")
        self.marca=raw_input("marca del producto:")
        self.serie=raw_input("serie del producto:")
    def imprimir(self):
        Credito.imprimir(self)
        print("datos del producto:")
        print"marca del Producto:"+str(self.marca)
        print"serie del Producto:"+str(self.serie)
        
                                                
        