from Clase_Convencional import Convencional
from Clase_No_Convencional import NoConvencional
from Fiduciario_Privado import Fiduciario_Privado
from Fiduciario_Publico import FiduciarioPublico
from Vehiculos_Y_Maquinaria import VehiculosYMaquinaria
from HipotecaPosesoria import HipotecaPosesoria
from HipotecarioReal import HipotecaReal    
import os 
class Principal(object):
    def principal(self):
        self.res=0
        while(self.res!=3):
            os.system('cls')
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
            else :
                print"error ingreso equivocado"
    def ingresar(self):
        os.system('cls')
        print".........¿que tipo de credito desea hacer?........."
        print"1.....................Hipoteca con Derechos Reales."
        print"2.................Hipoteca con Derechos Posesorios."
        print"3...................Credito con Fiduciario Publico."
        print"4.................Credito con Fiduciario Comercial."
        print"5....Credito con Garantia de Vehiculo / Maquinaria."
        print"6................Credito con Garantia convencional."
        print"7.............Credito con Garantia No Convencional."
        self.respuesta=raw_input("ingrese la opcion deseada:")
        if self.respuesta==1:
            hipotecareal=HipotecaReal()
            hipotecareal.imprimir()
            hipotecareal.guardar()
        elif self.respuesta==2:
            
    def buscar(self):
        pass

        