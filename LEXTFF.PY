def jogo_do_sapo():
    pedra_atual = 1
    pedra_final = 4

    print("Bem-vindo ao jogo do sapo!")
    print("Ajude o sapo a atravessar o rio pulandode pedra em pedra.\n")

    while pedra_atual < pedra_final:
        print(f"O sapo esta na pedra {pedra_atual}.")
        entrada = input("Digite o numero da prozima pedra (1 a 9): ")

        if not entrada.isdigit() or not (1 <= int(entrada) <= 9):
            print("Entrada invalida! O sapo saiu na agua. Fim de jogo.")
            return
        
        proxima_pedra = int(entrada)

        if proxima_pedra == pedra_atual + 1:
            print("Pulo correto!\n")
            pedra_atual += 1
        else:
            print("Pulo errado! O sapo caiu na agua. Fim de jogo.")
            return
        print("Parabens! O sapo chegou com sucesso a pedra 4!")

