#coding: utf-8
from string import Template
from Hipotecari import Hipoteca
class HipotecaPosesoria(Hipoteca):



    def __init__(self):
        Hipoteca.__init__(self,240)
        self.escritura=int(raw_input("Ingrese el numero de escritura del documento:"))
        self.nombremunicipalidad=raw_input("Ingrese el nombre de la municipalidad:")
    def calcular(self):
        self.cuota=self.monto*(0.015/(1-(1+0.015)**((self.cuotas)*-1)))
    def imprimir(self):
        Hipoteca.imprimir(self)
        print "numero de escritura:"+str(self.escritura)+"nombre de la muncipalidad:"+self.nombremunicipalidad
        print "las cuota es de: Q.%0.2f "%(self.cuota)
    def guardar(self):
        try:
            archivo=open("Archivos/HipotecaPosesoria.txt","a")
        except:
            archivo=open("Archivos/HipotecaPosesoria.txt","w")
        archivo.write(self.cliente.nombre+"\n"+self.cliente.segudnonombre+"\n"+self.cliente.primerapellido+"\n"+self.cliente.segundoapellido+"\n"+self.cliente.dirreccioncliente+"\n"+self.cliente.correocliente+"\n"+str(self.cliente.telfonocliente)+"\n"+str(self.monto)+"\n"+str(self.cuotas)+"\n"+str(self.cuota)+"\n"+str(self.libro)+"\n"+str(self.finca)+"\n"+str(self.folio)+"\n"+str(self.escritura)+self.nombremunicipalidad+"¬")
        archivo.close()
        
    
    def imprimir_web(self):
        html=self.leerplantilla("hipotecareal.html")
        diccionario=dict(
                         Nombre=self.cliente.nombre,
                         SNombre=self.cliente.segudnonombre,
                         PrimerApellido=self.cliente.primerapellido,
                         segundoapellido=self.cliente.segundoapellido,
                         telefono=self.cliente.segundoapellido,
                         correo=self.cliente.correo,
                         dirreccion=self.cliente.dirreccion,
                         numero=self.nocredito,
                         monto=self.monto,
                         cuotas=self.cuotas,
                         cuota=self.cuota,
                         finca=self.finca,
                         libro=self.libro,
                         folio=self.folio,
                         escritura=self.escritura,
                         municipalidad=self.nombremunicipalidad,
                         )
        html = Template(html).safe_substitute(diccionario)
        self.guardar(html,"hipotecareal.html")
        
        
        
        