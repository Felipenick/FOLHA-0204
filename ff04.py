numero_itens = int(input("Quantos itens pretende adicionar a lista de compras?"))

lista_compras = []

for i in range(numero_itens):
    item = input(f"Insira o nome do item {i+1}: ")

    lista_compras.append(item)

print("A sua lista de compras é:")
for item in lista_compras:
    print(item)