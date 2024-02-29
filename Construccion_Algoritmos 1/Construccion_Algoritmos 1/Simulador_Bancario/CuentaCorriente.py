class CuentaCorriente:
    #aqui va el codigo
    '''-------------------------------------
    # Atributos
    -------------------------------------'''
    valor=0
    
    '''-----------------------------------
    # Metodos
    -----------------------------------'''
    
    def ConsignarValor(self, valor):
        self.valor += valor
        return "se consignaron: " + (valor) + "a su cuenta."
    
    def RetirarValor(self, valor):
        if valor <= self.valor:
            self.valor -= valor
            return "se retiraron: " + (valor) + "de su cuenta."
        else:
            return "valor insuficiente para retirar: " + (valor) + "de su cuenta"
        
    def ConsultarValor(self):
        return "su valor actual es: 0" + (self.valor)
    