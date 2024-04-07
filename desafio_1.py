menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

'''

saldo = 0
LIMITE = 500
extrato = ''
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == '1':
        deposito = float(input('Informe o valor do deposito: '))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: + R$ {deposito:.2f}\n"        
            print(f'O valor: R$ {deposito} foi depositado com sucesso')
         
        else:
            print('Não foi possivel depositar o valor informado.')
        
    elif opcao == "2":
        saque = float(input('Informe o valor a ser sacado: '))
        
        if (numero_de_saques < LIMITE_DE_SAQUES) and (saque <= LIMITE) and (saque <= saldo):
            saldo -= sa
            extrato += f"Saque: - R$ {saque:.2f}\n"
            numero_de_saques += 1
        
        else:
            print('Não foi possivel sacar o valor informado.')
            
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    elif opcao == "0":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")