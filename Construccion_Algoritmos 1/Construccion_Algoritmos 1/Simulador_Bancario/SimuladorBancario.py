from CuentaCorriente import CuentaCorriente
from CuentaAhorros import CuentaAhorros

class SimuladorBancario:
    #aqui va el codigo
    '''--------------------------------------
    # Atributos
    --------------------------------------'''
    cedula=''
    Nombre=''
    Mesactual=0
    
    '''--------------------------------------------
    # Asociaciones
    --------------------------------------------'''
    corriente=CuentaCorriente()
    ahorros=CuentaAhorros()

    '''----------------------------------------------
    # Metodos
    ----------------------------------------------'''
    
    def ConsignarCuentaCorriente(self, valor):
        #aqui va el codigo
        self.corriente.ConsignarValor()
        
    def CalcularValorTotal(self):
        #aqui va el codigo
        return self.corriente.ConsultarValor() + self.ahorros.ConsultarValor()
    
    def PasarAhorrosACorriente(self):
        #aqui va el codigo 
        self.corriente.ConsignarValor(self.ahorros.ConsultarValor())