from classes.pessoa import Pessoa


class Cliente(Pessoa):
    def show_pessoa(self):
        print(self.nome, self.cpf)
