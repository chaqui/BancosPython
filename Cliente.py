#coding: utf-8
class Cliente1(object):
    def ingresar(self):
        self.nombre=raw_input("ingrese el pimer nombre del cliente nombre:")
        self.segudnonombre=raw_input("ingrese el segundo nombre del cliente:")
        self.primerapellido=raw_input("ingrese el primer apellido del cliente:")
        self.segundoapellido=raw_input("ingrese el segundo apellido del cliente:")
        self.correo=raw_input("ingrese el correo del cliente:")
        self.telfono=int(raw_input("ingrese el telefono del cliente:"))
        self.dirreccion=raw_input("ingrese la dirreccion del cliente:")
    def imprimir(self):
        a="/"*80
        print a
        print "datos del usuario:"
        print("el usuario es: "+self.nombre+" "+self.segudnonombre+" "+self.primerapellido+" "+self.primerapellido+" "+self.segundoapellido+"\n correo:"+self.correocliente+" \n telefono:"+str(self.telfonocliente)+"\n dirreccion:"+self.dirreccioncliente)