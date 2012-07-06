#coding: utf-8
from Garantia_Prendaria import GarantiaPrendaria
from Tarjeta_De_Circulacion import TarjetaDeCirculacion
from string import Template
class VehiculosYMaquinaria(GarantiaPrendaria):
    def __init__(self):
        GarantiaPrendaria.__init__(self,36)
        self.tarjetaDeCirculacion=TarjetaDeCirculacion()
    def imprimir(self):
        GarantiaPrendaria.imprimir(self)
        self.tarjetaDeCirculacion.imprimir()
        print"Cuota es de: Q.%f0.2"%(self.cuota)
    def calcular(self):
        self.cuota=self.monto*(0.015/(1-(1+0.015)**((self.cuotas)*-1)))
    def Guardar(self):
        try:
            archivo=open("Archivos/VehiculosYMaquinaria.txt","a")
        except:
            archivo=open("Archivos/VehiculosYMaquinaria.txt","w")
        archivo.write(self.cliente.nombre+"\n"+self.cliente.segudnonombre+"\n"+self.cliente.primerapellido+"\n"+self.cliente.segundoapellido+"\n"+self.cliente.dirreccioncliente+"\n"+self.cliente.correocliente+"\n"+str(self.cliente.telfonocliente)+"\n"+str(self.tarjetaDeCirculacion.numero)+"\n"+str(self.tarjetaDeCirculacion.fechaDeEmision)+"\n"+str(self.tarjetaDeCirculacion.fechaDeCaducidad)+"\n"+str(self.monto)+"\n"+str(self.cuotas)+"\n"+str(self.cuota)+"\n"+self.nocredito+"¬")
        archivo.close()
    def imprimir_web(self):
            html=self.leerplantilla("hml/vehiculosymaquinaria.html")
            diccionario=dict(
                         Nombre=self.cliente.nombre,
                         SNombre=self.cliente.segudnonombre,
                         PrimerApellido=self.cliente.primerapellido,
                         segundoapellido=self.cliente.segundoapellido,
                         telefono=self.cliente.segundoapellido,
                         correo=self.cliente.correo,
                         dirreccion=self.cliente.dirreccion,
                         numero=self.nocredito,
                         numerotarjeta=self.tarjetaDeCirculacion.numero,
                         fechaemision=self.tarjetaDeCirculacion.fechaDeEmision,
                         fechacaducidad=self.tarjetaDeCirculacion.fechaDeCaducidad,
                         monto=self.monto,
                         cuotas=self.cuotas,
                         cuota=self.cuota,
                              )
            html = Template(html).safe_substitute(diccionario)
            self.guardar(html,"html imprimir/vehiculosymaquinaria.html")
        