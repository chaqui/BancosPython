from creditofiduciario import CreditoFiduciario
class MyClass(CreditoFiduciario):
    def __init__(self):
        CreditoFiduciario.__init__(self)
    def calcular(self):
        self.cuota=self.monto*(0.01667/(1-(1+0.01667)**((self.cuotas)*-1)))
    
        