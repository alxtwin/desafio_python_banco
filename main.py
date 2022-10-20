from classes.banco import Banco
from time import sleep

cliente = Banco()
cliente.mensagem_bem_vindo()
opcao = input('Opção:')

if opcao == '1':
    cliente.cadastra_conta()
    cliente.menu()
    while True:

        menu = int(input())
        match menu:
            case 1:  #mostrar saldo
                cliente.mostra_saldo()
            case 2: #depositar
                cliente.depositar()
            case 3:
                cliente.sacar()
            case 5:
                quit()
            
elif opcao == '2':
    quit()

