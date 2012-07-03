from Garantia_Prendaria import GarantiaPrendaria
from Tarjeta_De_Circulacion import TarjetaDeCirculacion

class VehiculosYMaquinaria(GarantiaPrendaria):
    def __init__(self):
        GarantiaPrendaria.__init__(self)
        self.tarjetaDeCirculacion=TarjetaDeCirculacion()
        
        
        