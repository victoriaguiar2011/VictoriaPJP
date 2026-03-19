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
n3 = float(input("\nInforme um número decimal (Ex: X.X): "))
n4 = float(input("Informe outro número decimal (Ex: X.X): "))
media = (n3 + n4)/2
print(f'A média aritmética é: {media}')

#Leia um número como string e imprima o seu tipo antes e depois de converter para int.
numero_string = (input("\nInforme um número: "))
print(f'Antes da conversão: {type (numero_string)}.')
numero_int = int(numero_string)
print(f'Depois da conversão: {type (numero_int)}.')

#Leia o preço de um produto e imprima o preço com 10% de desconto
preco = float(input("\nInforme o preço do produto R$ XX.XX: "))
desconto = preco * 0.10
preco_final = preco - desconto
print(f'Preço com 10% de desconto: {preco_final}')

#Leia o raio de um círculo (float) e calcule a área, utilize π = 3.14.
raio = float(input("\nInforme o raio do círculo: "))
area = 3.14 * (raio ** 2)
print(f'A área do círculo é: {area:.2f}')

#Leia a distância (km) e o tempo (h), calcule a velocidade média
distancia = float(input("\nInforme a distância percorrida em km: "))
tempo = float(input("Informe o tempo demorado em horas: "))
velocidade = distancia // tempo
print(f'A velocidade média é: {velocidade}km por hora.')

#Leia 3 notas (float) e imprima a média com duas casas decimais.
nota1 = float(input("\nInforme a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Infrome a terceira nota: "))
media = (nota1 + nota2 + nota3)/3
print(f'A média aritmética é: {media: .2f}')

#Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.
salario = float(input("\nInforme o seu salário (sem ponto ou vírgula) R$: "))
aumento = salario * 0.10
novo_salario = salario + aumento
print(f'O novo salário com aumento de 10% é: {novo_salario}')

#Leia uma quantidade de minutos (int) e converta para horas e minutos
minutos = int(input("\nInforme o tempo em minutos: "))
horas = minutos // 60
resto = minutos % 60
print(f'{horas}h{resto}')

#Leia o nome e a idade e imprima exatamente neste formato
print(f'\nNome: {nome} | Idade: {idade} anos')

#Leia dois int (a e b) e imprima:
a = int(input("\nInforme um número inteiro: "))
b = int(input("Informe outro número inteiro: "))
print(f'{a} + {b} = X | {a} - {b} = Y | {a} * {b} = Z')

#Leia um float e imprima com 2 casas decimais
f_num = float(input("\nInforme um número qualquer: "))
print(f'{f_num: .2f}')

#Leia um nome e uma nota (float), com uma casa decimal, e imprima:
aluno = nome
a_nota = float(input("\nInforme a sua nota: "))
print(f'{aluno} ficou com nota {a_nota}')

#Leia o ano de nascimento (int) e imprima a idade estimada. (considere ano atual = 2026).
ano_nasc = int(input("\nInforme o ano do seu nascimento: "))
ano_atual = 2026
est_idade = ano_nasc - ano_atual
print(f'Você tem {est_idade} anos.')