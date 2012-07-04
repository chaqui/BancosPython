#coding: utf-8
from Clase_Convencional import Convencional
from Clase_No_Convencional import NoConvencional
from Fiduciario_Privado import Fiduciario_Privado
from Fiduciario_Publico import FiduciarioPublico
from Vehiculos_Y_Maquinaria import VehiculosYMaquinaria
from HipotecaPosesoria import HipotecaPosesoria
from HipotecarioReal import HipotecaReal    
class Principal(object):
    def principal(self):
        self.res=0
        while(self.res!=2):
            print"¿que desea hacer?"
            print"ingresar cliente.......0"
            print"buscar cliente.........1"
            print"salir..................2"
            self.respuesta=int(raw_input("Ingrese su respuesta:"))
            if self.respuesta==0 :
                self.ingresar()
                self.res=raw_input("¿desea regresar al menu? (1=si,2=no)")
            elif self.respuesta==1:
                self.buscar()
                self.res=raw_input("¿desea regresar al menu? (1=si,2=no)")
            elif self.respuesta==2:
                print"saliendo.."
                self.res=2
            else :
                print"error ingreso equivocado"
    def ingresar(self):
        print".........¿que tipo de credito desea hacer?........."
        print"1.....................Hipoteca con Derechos Reales."
        print"2.................Hipoteca con Derechos Posesorios."
        print"3...................Credito con Fiduciario Publico."
        print"4.................Credito con Fiduciario Comercial."
        print"5....Credito con Garantia de Vehiculo / Maquinaria."
        print"6................Credito con Garantia convencional."
        print"7.............Credito con Garantia No Convencional."
        self.respuesta=int(raw_input("ingrese la opcion deseada:"))
        if self.respuesta==1:
            print"1"
            hipotecareal=HipotecaReal()
            hipotecareal.imprimir()
            hipotecareal.guardar()
        elif self.respuesta==2:
            hipotecaposesoria=HipotecaPosesoria()
            hipotecaposesoria.imprimir()
            hipotecaposesoria.guardar()
        elif self.respuesta==3:
            fiduciariopublico=FiduciarioPublico()
            fiduciariopublico.imprimir()
            fiduciariopublico.guardar()
        elif self.respuesta==4:
            fiduciarioprivado=Fiduciario_Privado()
            fiduciarioprivado.imprimir()
            fiduciarioprivado.guardar()
        elif self.respuesta==5:
            vehiculosymaquinaria=VehiculosYMaquinaria()
            vehiculosymaquinaria.Guardar()
            vehiculosymaquinaria.imprimir()
        elif self.respuesta==6:
            convencional=Convencional()
            convencional.guardar()
            convencional.imprimir()
        elif self.respuesta==7:
            noconvencional= NoConvencional()
            noconvencional.guardar()
            noconvencional.imprimir()
    def buscar(self):
        pass
principal=Principal()
principal.principal()

        