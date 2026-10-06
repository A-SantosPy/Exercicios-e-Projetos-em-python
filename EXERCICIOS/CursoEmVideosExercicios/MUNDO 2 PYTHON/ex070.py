print('-' * 30)
print('LOJA SUPER BARATA')
print('-' * 30)
total = 0
mais_1000 = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))
    total += preco
    if preco > 1000:
        mais_1000 += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break

print(f'Total da compra: R$ {total:.2f}')
print(f'Quantidade de produtos acima de R$ 1000: {mais_1000}')