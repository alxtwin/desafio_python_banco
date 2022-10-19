from classes.cliente import Cliente
from random import randint


class Conta(Cliente):
    def __init__(self, agencia=0, senha=0, tipo_conta=''):
        self.agencia = agencia
        self.senha = senha
        self.tipo_conta = tipo_conta

