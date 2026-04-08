#Desafio 1
def bem_vindo(nome):
    print(f"Bem vindo, {nome}")

bem_vindo("Victória")

#Desafio 2
def somar(a,b):
    return a + b

resultado = somar(10,5)
print(f'Soma: {resultado}')

#Desafio 3
def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")

par_ou_impar(7)
par_ou_impar(4)

#Desafio 4
def maior_numero(lista):
    return max(lista)

numero = [3,17,8,42,5,1]
print(f"Maior número: {maior_numero(numero)}")

#Desafio 5
def conta_caracteres(texto):
    return len(texto)

print(f"Quantidade de caracteres: {conta_caracteres("Olá, mundo")}")

#Desafio 6
def calcular_media(lista):
    return sum(lista)/len(lista)
valores = [10,20,30,40,50]
print(f"media:{calcular_media(valores):.2f}")

#Desafio 7
def palindromo(palavra):
palavra_limpa = palavra.lower().replace(" ", "")
    if palavra_limpa == palavra_limpa[::-1]
        print(f"'{palavra}' é um palíndromo!")
    else:
        print(f"'{palavra}' não é um palíndromo.")

palindromo("arara")
palindromo("python")
palindromo("ana")