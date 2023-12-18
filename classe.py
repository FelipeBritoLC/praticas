class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

aluno1 = Aluno(84938264, 'Felipe')
aluno2 = Aluno(84938644, 'Thayna')
        
print(aluno1.nome, aluno1.matricula)
print(aluno2.nome, aluno2.matricula)