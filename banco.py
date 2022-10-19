""" Aqui ficam as operações principais do banco..."""
from msilib.schema import Error
from classes.conta import Conta
from random import randint


class Banco(Conta):

    def gera_agencia(self):
        try:
            self.agencia = randint(1000, 9999)
            return self.agencia
        except Exception:
            return 'erro inesperado'

    def cadastra_conta(self):
        self.nome = input('Digite seu nome: ')
        self.cpf = input('Digite seu CPF')
        self.senha = input('Digite sua senha:')

    def mostra_conta(self):
        print(f'nome do titular: \n{self.nome}')
        print(f'cpf do titular: \n{self.cpf}')
        print(f'agência: \n{self.agencia}')
