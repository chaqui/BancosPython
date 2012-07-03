'''
Created on 3/07/2012

@author: josuechaqui
'''

class TarjetaDeCirculacion(object):
    def __init__(self):
        print("Profavor ingrese los datos de la circulacion.")
        self.fechaDeEmision=raw_input("ingrese la fecha de emision de la tarjeta:")
        self.fechaDeCaducidad=raw_input("ingres la fecha de caducidad de la tarjeta:")
        self.numero=int(raw_input("ingrese el numero de la tarjeta de circulacion:"))