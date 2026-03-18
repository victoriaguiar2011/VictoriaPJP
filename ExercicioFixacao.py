#Peça ao usuário seu nome e cumprimente utilizando a função print(), ex.: "Olá, Carol!"
nome = input("Informe o seu nome: ") 
print(f'Olá, {nome}!')

#Peça ao usuário sua idade e exiba na tela: "Você tem {idade} anos!"
idade = input("\nInforme a sua idade: ") 
print(f'Você tem {idade} anos!')

#Leia o nome e a cidade da pessoa e imprima: "{nome} mora em {cidade}."
cidade = input("\nInforme a sua cidade: ")
print(f'{nome} mora em {cidade}.')

#Leia um número e imprima o dobro dele.
numero = int(input("\nInforme um número inteiro qualquer para calcular o dobro: "))
dobro = numero * 2
print(f'O dobro de {numero} é {dobro}.')

#Leia dois números inteiros e imprima a soma.
n1 = int(input("\nInforme um número inteiro: "))
n2 = int(input("Informe outro número inteiro para somar: "))
soma =  n1 + n2
print(f'A soma de {n1} com {n2} é {soma}.')

#Leia a altura (em metros) como float e imprima: "Sua altura é {altura}m"
altura = float(input("\nInforme a sua altura (Ex: 1.74): "))
print(f'Sua altura é {altura}m.')

#Leia dois números decimais (float) e imprima a média
n3 = float(input("\ninforme um número decimal (Ex: X.X): "))
n4 = float(input("Informe outro número decimal (Ex: X.X): "))
media = (n3 + n4)/2
print(f'A média aritmética é: {media}')

#Leia um número como string e imprima o seu tipo antes e depois de converter para int.
numero_string = (input("\nInforme um número: "))
print(f'Antes da conversão: {type (numero_string)}.')
numero_int = int(numero_string)
print(f'Depois da conversão: {type (numero_int)}.')