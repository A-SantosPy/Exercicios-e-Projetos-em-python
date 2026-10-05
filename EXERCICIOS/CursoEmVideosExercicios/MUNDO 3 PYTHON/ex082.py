# Listas para armazenar os números
valores = []
pares = []
impares = []

# Loop para leitura dos dados
while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    
    # Pergunta se o usuário quer continuar
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    if resp == 'N':
        break

# Separação dos valores em pares e ímpares
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

# Exibição dos resultados na tela
print('-=' * 30)
print(f'A lista completa é: {valores}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')
