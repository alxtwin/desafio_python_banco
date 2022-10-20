class Pessoa:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoa):
    def show_pessoa(self):
        print(self.nome, self.cpf)
