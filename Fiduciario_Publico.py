#coding: utf-8
from string import Template
from creditofiduciario import CreditoFiduciario
class FiduciarioPublico(CreditoFiduciario):
    def __init__(self):
        CreditoFiduciario.__init__(self,270)
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
        archivo.write(self.cliente.nombre+" "+self.cliente.segudnonombre+" "+self.cliente.primerapellido+" "+self.cliente.segundoapellido+" "+self.cliente.dirreccioncliente+" "+self.cliente.correocliente+" "+str(self.cliente.telfonocliente)+" "+self.fiduciario1.nombre+" "+self.fiduciario1.segudnonombre+" "+self.fiduciario1.primerapellido+" "+self.fiduciario1.segundoapellido+" "+str(self.fiduciario1.telfono)+" "+self.fiduciario1.correo+" "+self.fiduciario1.dirreccion+" "+str(self.monto)+" "+str(self.cuotas)+" "+str(self.cuota)+" "+str(self.libro)+" "+str(self.finca)+" "+str(self.folio)+" "+str(self.escritura)+self.nombremunicipalidad+"¬")
        archivo.close()
    def imprimir_web(self):
            html=self.leerplantilla("hml/Publico.html")
            diccionario=dict(
                         Nombre=self.cliente.nombre,
                         SNombre=self.cliente.segudnonombre,
                         PrimerApellido=self.cliente.primerapellido,
                         segundoapellido=self.cliente.segundoapellido,
                         telefono=self.cliente.segundoapellido,
                         correo=self.cliente.correo,
                         dirreccion=self.cliente.dirreccion,
                         numero=self.nocredito,
                         Nombrefid=self.cliente.nombre,
                         SNombrefid=self.cliente.segudnonombre,
                         PrimerApellidofid=self.cliente.primerapellido,
                         segundoapellidofid=self.cliente.segundoapellido,
                         telefonofid=self.cliente.segundoapellido,
                         correofid=self.cliente.correo,
                         dirreccionfid=self.cliente.dirreccion,
                         numerofid=self.nocredito,
                         montofid=self.monto,
                         cuotas=self.cuotas,
                         cuota=self.cuota,
                         
                         )
            html = Template(html).safe_substitute(diccionario)
            self.guardar(html,"html imprimir/Publico.html")
        