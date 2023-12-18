from cliente import Cliente

class ContaCorrente:
    def __init__(self, valor, status, cliente):
        self.__valor = valor
        self.status = status
        self.cliente = cliente
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, novo_valor):
        if novo_valor >= 0:
            self.__valor = novo_valor

    def __str__(self):
        return f'A conta possui um valor de {self.__valor} e seu status é: {self.status}, {self.cliente}.'



cliente = Cliente('Felipe', 15418781405)
Conta1 = ContaCorrente(1500, 'ativa', cliente)

Conta1.valor = 8790

print(Conta1)


