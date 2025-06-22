menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITES_SAQUES = 3 

while True:
    
    opcao = input(menu).upper()

    if opcao == "D":
        valor_deposito = float(input("Valor do Depósito: R$"))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Deposito no valor de R${valor_deposito:.2f}\n"
        else:
            print("Operação não realizada!")

    elif opcao == "S":
        valor_saque = float(input("Valro do Saque: R$"))
        if numeros_saques != 3:
            if valor_saque <= saldo and valor_saque <= limite and numeros_saques != 3:
                saldo -= valor_saque
                numeros_saques += 1
                extrato += f"Saque no valor de R${valor_saque:.2f}\n"
            else:
                print("Operação não realizada!")
        else:
                print("Limite de saques atingido")
    elif opcao == "E":
        print("###EXTRATO###")
        print("Sem movimentações fiannceiras" if not extrato else extrato)
        print(f"Saldo: R${saldo}")

    elif opcao == "Q":
        break
    else:
        print("Operação inválida")