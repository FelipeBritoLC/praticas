class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf
   
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def __str__(self):
        return f'Cliente: {self.nome}, cpf: {self.__cpf}.'
    
