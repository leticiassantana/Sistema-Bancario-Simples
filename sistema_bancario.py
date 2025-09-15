menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato +=f"Deposito de {valor:.2f}\n"

        else:
            print("Operação falhou! Ooção inválida.")
    
    if opcao == "2":
        valor = float(input("Informe o valor do saque: "))