from creditofiduciario import CreditoFiduciario
class MyClass(CreditoFiduciario):
    def __init__(self):
        CreditoFiduciario.__init__(self)
    def calcular(self):
        self.cuota=self.monto*(0.01667/(1-(1+0.01667)**((self.cuotas)*-1)))
    def imprimir(self):
        CreditoFiduciario.imprimir(self)
        print"Cuota es de: Q.%f0.2"%(self.cuota)
    def guardar(self):
        try:
            archivo=open("Archivos/FiduciarioPublico.txt","a")
        except:
            archivo=open("Archivos/FiduciarioPublico.txt","w")
        archivo.write(self.cliente.nombre+" "+self.cliente.segudnonombre+" "+self.cliente.primerapellido+" "+self.cliente.segundoapellido+" "+self.cliente.dirreccioncliente+" "+self.cliente.correocliente+" "+str(self.cliente.telfonocliente)+" "+str(self.monto)+" "+str(self.cuotas)+" "+str(self.cuota)+" "+str(self.libro)+" "+str(self.finca)+" "+str(self.folio)+" "+str(self.escritura)+self.nombremunicipalidad+"¬")
        archivo.close()
        