dados_pessoas = []
for i in range(3):
    print(f"\nPessoa {i+1}:")
    nome = input("Digite o nome: ")
    filme = input("Qual filme asssitiu? ")
    while True:
        try:
            nota = float(input("Qual a nota do filme (0 a 10)? "))
            if 0 <= nota <=10:
                break
            else:
                print("Nota invalida")
        except ValueError:
            print("Por favor digite uma nota que seja valida")
pessoa = {
    "nome": nome,
    "filme": filme,
    "nota": nota
}
dados_pessoas.append(pessoa)

print("\Dados coletados:")
for pessoa in dados_pessoas:
    print(f"{pessoa['nome']} assistiu '{pessoa['filme']} e deu nota {pessoa['nota']}")