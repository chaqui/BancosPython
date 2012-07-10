#coding: utf-8
class Buscar(object):
    def __init__(self):
        self.busqueda1=raw_input("ingrese el nombre a buscar: ")
        self.Busqueda()
    def Busqueda(self):
        self.archivo=('Archivos/Clase_Convencional.txt','Clase_No_Convencional.txt','Archivos/Fiduciario_Privado.txt','Archivos/FiduciarioPublico.txt','Archivos/HipotecaPosesoria.txt','Archivos/HipotecaReal.txt','VehiculosYMaquinaria.txt')
        self.a=self.Convencional(self.archivo[0])
        if self.a==False:
            self.a=self.Noconvencional(self.archivo[1])
            if self.a==False:
                self.a=self.Privado(self.archivo[2])
                if self.a==False:
                    self.a=self.publico(self.archivo[3])
                if self.a==False:
                    self.a=self.Posesorio(self.archivo[4])
                    if self.a==False:
                        self.a=self.Real(self.archivo[5])
                        if self.a==False:
                            self.a=self.Herramientas(self.archivo[6])
                            if self.a==False:
                                print"archivo no encontrado"
        
    def Convencional(self,archivo):
        try:
            self.file=open(archivo,"r")
            self.dato="n"
            self.b=0
            self.a=False
            while(self.dato!=" "):
                self.b=self.b+1
                self.dato=self.file.readline()
                if (self.dato==self.busqueda1 and ((self.b/14==0) or (self.b==1))):
                    print"se encontro el cliente los datos son:"
                    print"primer nombre del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"segundo nombre del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print "segundo apellido del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "la dirreccion  del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el correo del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el telefono del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el monto del credito es:"+ self.dato
                    self.dato=self.file.readline()
                    print "las cuotas del credito es:"+ self.dato
                    self.dato=self.file.readline()
                    print "su cuota es:"+ self.dato
                    self.dato=self.file.readline()
                    print "el tipo de producto es:"+ self.dato
                    self.dato=self.file.readline()
                    print "la cantidad de productos es:"+ self.dato
                    self.dato=self.file.readline()
                    print "el costo de productos son:"+ self.dato
                    self.dato=self.file.readline()
                    self.a=True
                    break 
        except:
            self.a=False        
            return self.a
    def Noconvencional(self,archivo):
        try:
            self.file=open(archivo,"r")
            self.dato="n"
            self.b=0
            self.a=False
            while(self.dato!=" "):
                self.b=self.b+1
                self.dato=self.file.readline()
                if (self.dato==self.busqueda1 and ((self.b/14==0) or (self.b==1))):
                    print"se encontro el cliente los datos son:"
                    print"primer nombre del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"segundo nombre del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print "segundo apellido del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "la dirreccion  del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el correo del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el telefono del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el monto del credito es:"+ self.dato
                    self.dato=self.file.readline()
                    print "las cuotas del credito es:"+ self.dato
                    self.dato=self.file.readline()
                    print "su cuota es:"+ self.dato
                    self.dato=self.file.readline()
                    print "el tipo de producto es:"+ self.dato
                    self.dato=self.file.readline()
                    print "la cantidad de productos es:"+ self.dato
                    self.dato=self.file.readline()
                    print "el costo de productos son:"+ self.dato
                    self.dato=self.file.readline()
                    self.a=True
                    break 
        except:
            self.a=False    
        return self.a
    def Privado(self,archivo):
        try:
            self.file=open(archivo,"r")
            self.dato="n"
            self.b=0
            self.a=False
            while(self.dato!=" "):
                self.b=self.b+1
                self.dato=self.file.readline()
                if (self.dato==self.busqueda1 and ((self.b/14==0) or (self.b==1))):
                    print"se encontro el cliente los datos son:"
                    print"primer nombre del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"segundo nombre del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print "segundo apellido del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "la dirreccion  del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el correo del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el telefono del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print"primer nombre del fiduciario: "+self.dato
                    self.dato=self.file.readline()
                    print"segundo nombre del fiducioario: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del fiduciario: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del fiduciario: "+self.dato
                    self.dato=self.file.readline()
                    print "segundo apellido del fiduciario:"+ self.dato
                    self.dato=self.file.readline()
                    print "la dirreccion  del fiduciario:"+ self.dato
                    self.dato=self.file.readline()
                    print "el correo del fiduciario:"+ self.dato
                    self.dato=self.file.readline()
                    print "el telefono del fiduciario:"+ self.dato
                    self.dato=self.file.readline()
                    print "el monto del credito es:"+ self.dato
                    self.dato=self.file.readline()
                    print "las cuotas del credito es:"+ self.dato
                    self.dato=self.file.readline()
                    print "su cuota es:"+ self.dato
                    self.dato=self.file.readline()
                    print "el tipo de producto es:"+ self.dato
                    self.dato=self.file.readline()
                    print "la cantidad de productos es:"+ self.dato
                    self.dato=self.file.readline()
                    print "el costo de productos son:"+ self.dato
                    self.dato=self.file.readline()
                    self.a=True
                    break 
        except:
            self.a=False        
            return self.a
    def publico(self,archivo):
        try:
            self.file=open(archivo,"r")
            self.dato="n"
            self.b=0
            self.a=False
            while(self.dato!=" "):
                self.b=self.b+1
                self.dato=self.file.readline()
                if (self.dato==self.busqueda1 and ((self.b/14==0) or (self.b==1))):
                    print"se encontro el cliente los datos son:"
                    print"primer nombre del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"segundo nombre del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print "segundo apellido del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "la dirreccion  del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el correo del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el telefono del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print"primer nombre del fiduciario: "+self.dato
                    self.dato=self.file.readline()
                    print"segundo nombre del fiducioario: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del fiduciario: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del fiduciario: "+self.dato
                    self.dato=self.file.readline()
                    print "segundo apellido del fiduciario:"+ self.dato
                    self.dato=self.file.readline()
                    print "la dirreccion  del fiduciario:"+ self.dato
                    self.dato=self.file.readline()
                    print "el correo del fiduciario:"+ self.dato
                    self.dato=self.file.readline()
                    print "el telefono del fiduciario:"+ self.dato
                    self.dato=self.file.readline()
                    print "el monto del credito es:"+ self.dato
                    self.dato=self.file.readline()
                    print "las cuotas del credito es:"+ self.dato
                    self.dato=self.file.readline()
                    print "su cuota es:"+ self.dato
                    self.dato=self.file.readline()
                    print "el tipo de producto es:"+ self.dato
                    self.dato=self.file.readline()
                    print "la cantidad de productos es:"+ self.dato
                    self.dato=self.file.readline()
                    print "el costo de productos son:"+ self.dato
                    self.dato=self.file.readline()
                    self.a=True
                    break 
        except:
            self.a=False        
            return self.a
    def Posesorio(self,archivo):
        try:
            self.file=open(archivo,"r")
            self.dato="n"
            self.b=0
            self.a=False
            while(self.dato!=" "):
                self.b=self.b+1
                self.dato=self.file.readline()
                if (self.dato==self.busqueda1 and ((self.b/14==0) or (self.b==1))):
                    print"se encontro el cliente los datos son:"
                    print"primer nombre del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"segundo nombre del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print "segundo apellido del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "la dirreccion  del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el correo del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el telefono del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el monto del credito es:"+ self.dato
                    self.dato=self.file.readline()
                    print "las cuotas del credito es:"+ self.dato
                    self.dato=self.file.readline()
                    print "su cuota es:"+ self.dato
                    self.dato=self.file.readline()
                    print "el libro es:"+ self.dato
                    self.dato=self.file.readline()
                    print "la finca es: "+ self.dato
                    self.dato=self.file.readline()
                    print "el folio es :"+ self.dato
                    self.dato=self.file.readline()
                    print "el numero de escritura es :"+ self.dato
                    self.dato=self.file.readline()
                    print "el nombre de la municipalidad es :"+ self.dato
                    
                    self.a=True
                    break 
        except:
            self.a=False    
        return self.a
    def Real(self,archivo):
        return self.a    
    def Herramientas(self,archivo):
        try:
            self.file=open(archivo,"r")
            self.dato="n"
            self.b=0
            self.a=False
            while(self.dato!=" "):
                self.b=self.b+1
                self.dato=self.file.readline()
                if (self.dato==self.busqueda1 and ((self.b/14==0) or (self.b==1))):
                    print"se encontro el cliente los datos son:"
                    print"primer nombre del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"segundo nombre del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print"primer apellido del cliente: "+self.dato
                    self.dato=self.file.readline()
                    print "segundo apellido del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "la dirreccion  del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el correo del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el telefono del cliente:"+ self.dato
                    self.dato=self.file.readline()
                    print "el numero de tajeta de circulacion es:"+ self.dato
                    self.dato=self.file.readline()
                    print "la fecha de caducidad de la tarjeta de circulacion es:"+ self.dato
                    self.dato=self.file.readline()
                    print "la fecha de  emision de la tarjeta de circulacion es:"+ self.dato
                    self.dato=self.file.readline()
                    print "el monto del credito es:"+ self.dato
                    self.dato=self.file.readline()
                    print "las cuotas del credito es:"+ self.dato
                    self.dato=self.file.readline()
                    print "su cuota es:"+ self.dato
                    self.dato=self.file.readline()
                    print "el numero de credito es:"+ self.dato
                    self.dato=self.file.readline()
                    self.a=True
                    break     
        except:
            self.a=False
        return self.a
            