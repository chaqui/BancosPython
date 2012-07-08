#coding: utf-8
from Garantia_Prendaria import GarantiaPrendaria
from produccion import Producto
from string import Template
class Convencional(GarantiaPrendaria):
    def __init__(self):
        GarantiaPrendaria.__init__(self,12)
        self.producto=Producto()
    def calcular(self):
        self.cuota=self.monto*(0.01667/(1-(1+0.01667)**((self.cuotas)*-1)))
    def imprimir(self):
        GarantiaPrendaria.imprimir(self)
        self.producto.imprimir()
        print"las cuota es: "+self.cuota
    def guardar(self):
        try:
            archivo=open("Archivos/Clase_Convencional.txt","a")
        except:
            archivo=open("Archivos/Clase_Convencional.txt","w")
        archivo.write(self.cliente.nombre+"\n"+self.cliente.segudnonombre+"\n"+self.cliente.primerapellido+"\n"+self.cliente.segundoapellido+"\n"+self.cliente.dirreccioncliente+"\n"+self.cliente.correocliente+"\n"+str(self.cliente.telfonocliente)+"\n"+str(self.monto)+"\n"+str(self.cuotas)+"\n"+str(self.cuota)+str(self.producto.tipo)+"\n"+str(self.producto.cantidad)+"\n"+str(self.producto.costo)+"¬")
        archivo.close()
    def imprimir_web(self):
            html=self.leerplantilla("hml/convencional.html")
            diccionario=dict(
                         Nombre=self.cliente.nombre,
                         SNombre=self.cliente.segudnonombre,
                         PrimerApellido=self.cliente.primerapellido,
                         segundoapellido=self.cliente.segundoapellido,
                         telefono=self.cliente.segundoapellido,
                         correo=self.cliente.correo,
                         dirreccion=self.cliente.dirreccion,
                         numero=self.nocredito,
                         tipo=self.producto.tipo,
                         cantidad=self.producto.cantidad,
                         costo=self.producto.costo,
                         monto=self.monto,
                         cuotas=self.cuotas,
                         cuota=self.cuota,
                              )
            html = Template(html).safe_substitute(diccionario)
            self.guardar(html,"html imprimir/convencional.html")
        
        
        
        