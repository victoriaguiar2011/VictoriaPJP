list1 = []
print(list1)
list1.append("canetas")
print(list1)
list1.extend(["garrafa", "caderno", "mochila"])
print(list1)
list1.remove("canetas")
print(list1)

lista_num_int = [
    int(input("Digite o 1º número: ")),
    int(input("Digite o 2º número: ")),
    int(input("Digite o 3º número: ")),
    int(input("Digite o 4º número: "))
]
print(f"Tamanho antes: {len(lista_num_int)}")
alvo = int(input("Digite o valor a remover: "))
if alvo in lista_num_int:
    lista_num_int.remove(alvo)
print(f"Tamanho depois: {len(lista_num_int)}")