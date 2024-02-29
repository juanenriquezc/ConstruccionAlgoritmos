class SimuladorBancario:
    #aqui va el codigo
    '''--------------------------------------
    # Atributos
    --------------------------------------'''
    cedula=''
    Nombre=''
    Mesactual=0
    saldo=0
    tasa_interes_mensual=0.02

    '''----------------------------------------------
    # Metodos
    ----------------------------------------------'''
    def ConsignarValor(self, valor):
        self.saldo += valor
        return "se retiraron 0" + (valor) + "a su cuenta."
    
    def RetirarValor(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return "se retiraron 0" + (valor) + "de su cuenta."
        else:
            return "saldo insuficiente para retirar 0" + (valor) + "de su cuenta"
        
    def ConsultarSaldo(self):
        return "su saldo actual es: 0" + (self.saldo)
    
    def ConsultarInteresMensual(self):
        interes_mensual= self.saldo * self.tasa_interes_mensual
        return "El interes mensual de su cuenta es: 0" + (interes_mensual)