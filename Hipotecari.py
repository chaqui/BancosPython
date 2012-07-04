#coding: utf-8
import Credito
class Hipoteca(Credito.Credito):
    def __init__(self,maximo):
        Credito.Credito.__init__(self,maximo)
        self.libro=int(input("ingrese el libro del documento:"))
        self.folio=int(input("ingrese el folio del documento:"))
        self.finca=int(input("ingrese la finca del documento:"))
    def imprimir(self):
        Credito.Credito.imprimir(self)
        print("libro:"+str(self.libro)+"folio:"+str(self.folio)+" finca:"+str(self.finca))
    



        
        