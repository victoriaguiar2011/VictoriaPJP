total_compras = 0
quantidade = 0

valor = float(input("Informe o valor da compra (0 para encerrar): "))

while valor != 0:
    total_compras += valor 
    quantidade += 1

    valor = float(input("Digite o valor da compra (0 para encerrar): "))

if quantidade > 0:
    media_compras = total_compras / quantidade
else:
    media_compras = 0

print(f"Total das compras: R$ {total_compras:.2f}")
print(f"Quantidade de compras: {quantidade}")
print(f"Valor médio das compras: R$ {media_compras:.2f}")

