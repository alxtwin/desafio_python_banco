""" Aqui ficam as operações principais do banco..."""
from queue import Empty
from classes.pessoa import Cliente
from random import randint
import maskpass


class Conta(Cliente):
    def __init__(self, agencia=0, conta=0, senha='', tipo_conta='', limite_conta=0, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.senha = senha
        self.tipo_conta = tipo_conta
        self.limite_conta = limite_conta
        self.saldo = saldo


class Banco(Conta):

    def mensagem_bem_vindo(self):
        print('Bem vindo ao Banco do Python.')
        print()
        print("---"*10)
        print('selecione a operação desejada:')
        print('---'*10)
        print('1 - Abrir conta')
        print('2 - Sair')
        print("---"*10)


    def menu(self):
        print()
        print('---'*10)
        print('Selecione a operação desejada:')
        print('---'*10)
        print('1 - Consultar saldo')
        print('2 - Depositar')
        print('3 - Sacar')
        print('4 - Sair')
        print("---"*10)


    def gera_agencia(self):
        try:
            self.agencia = randint(10, 500)
            self.agencia = str(self.agencia) 
            return self.agencia
        except Exception:
            return 'erro inesperado'

    def gera_conta(self):
        digito = 0
        self.conta = randint(1000, 9999)
        digito = randint(0, 9)
        self.conta = str(self.conta) + '-' + str(digito)
        return self.conta

    def cadastra_conta(self):
        print('Escolha o tipo de conta:')
        print('1 - Conta Corrente\n2 - Conta Poupança\n')
        tipo_conta = input()
        match tipo_conta:
            case 'corrente':
                self.tipo_conta = 'corrente'
                self.limite_conta = 1000.00
            case 'poupança':
                self.tipo_conta = 'poupança'
                self.limite_conta = 500.00
        self.nome = input('Digite seu nome:\n ')
        self.cpf = input('Digite seu CPF:\n ')
        self.senha = maskpass.askpass(prompt="Crie uma senha:\n ", mask="*")
        self.agencia = self.gera_agencia()
        self.conta = self.gera_conta()
        print("---"*10)
        depositar = input('Deseja depositar algum valor? [S/N]\n ')
        if depositar == 'S':
            self.depositar()

    # def checa_senha(self):
    #     senha = maskpass.askpass(prompt="Digite sua senha:\n ", mask="*")
    #     n = 0
    #     while n <= 2:
    #         if senha == self.senha:
    #             return True
    #         elif senha != self.senha:
    #             print('Senha incorreta!')
    #             n += 1
    #             print(f'você tem mais {n} tentativas')
    #             if n == 2:
    #                 print('Senha incorreta 3 vezes. Tente novamente mais tarde.')
    #                 break
    #             else:
    #                 self.checa_senha()
        
    def depositar(self):
        self.checa_senha()
        deposito = float(input('Digite o valor do depósito:\n '))
        print('Depósito realizado com sucesso!')
        self.saldo += deposito
        print(f'Seu saldo atual é de R$ {self.saldo}')
        choice = input('Deseja realizar outra operação? [S/N]\n ')
        choice.upper()
        if choice =='S':
            self.depositar()
        elif choice == 'N':
            self.menu() 
            
    def sacar(self):
        self.checa_senha()
        saque = float(input('Digite o valor do saque:\n '))
        if saque > self.saldo and saque < self.limite_conta:
            print('saldo insuficiente/limite de saque excedido.')
            return False
        else:
            self.saldo -= saque
            print('Saque realizado com sucesso!')
            print(f'Seu saldo atual é de R$ {self.saldo}')
            choice = input('Deseja realizar outra operação? [S/N]\n ')
            choice.upper()
            if choice == 'S':
                self.sacar()
            elif choice == 'N':
                self.menu()
    
    def mostra_saldo(self):
        print(f'nome do titular: \n{self.nome}'.upper())
        print()
        print(f'cpf do titular: {self.cpf}')
        print()
        print(f'agência: {self.agencia}, conta: {self.conta}')
        print(f'tipo de conta: {self.tipo_conta.upper()}; limite de saque: R$ {self.limite_conta}')
        print()
        print(f'saldo: \nR$ {self.saldo}')
        if (self.saldo >= 5000):
            print(
                'Sabia que você pode investir seu dinheiro? Selecione a opção 0 para saber mais.')
            
        choice = input('sair? [S/N]\n ')
        choice.upper()
        if choice == 'S':
            self.menu()
        elif choice == 'N':
            self.mostra_saldo()

