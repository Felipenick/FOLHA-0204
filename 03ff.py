def simular_caixa_eletronico():
    saldo_disponivel = 100 

    while True:
        try:
            valor_saque = float(input("Digite o valor a ser sacado (em reais): "))
            if valor_saque <= 0:
                print("Valor invalido. Digite um valor maior que zero.")
                continue
            if valor_saque > saldo_disponivel:
                print("Saldo insuficiente.")
                continue
            break 
        except ValueError:
            print("Entrada invalida. Digite um numero.")

    notas_50 = int(valor_saque // 50)
    valor_saque %= 50
    notas_20 = int(valor_saque // 20)
    valor_saque %=20
    notas_10 = int(valor_saque // 10)
    valor_saque %=10
    notas_05 = int(valor_saque // 5)
    valor_saque %=5
    notas_02 = int(valor_saque // 2)
    valor_saque %=2

    print("\nNotas a serem entregues:")
    if notas_50 > 0:
        print(f"{notas_50} notas de R$50")
    if notas_20 > 0:
        print(f"{notas_20} notas de R$20")
    if notas_10 > 0:
        print(f"{notas_10} notas de R$10")
    if notas_05 > 0:
        print(f"{notas_05} notas de R$05")
    if notas_02 > 0:
        print(f"{notas_02} notas de R$02")


    print(f"Total: R${valor_saque} ")