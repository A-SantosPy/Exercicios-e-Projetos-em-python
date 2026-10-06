print('-' * 30)
print('CADASTRO DE PESSOAS')
print('-' * 30)

idades = []
homens = 0
mulheres_menos_20 = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    idades.append(idade)
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break

print(f'Total de pessoas cadastradas: {len(idades)}')  
print(f'Total de homens: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres_menos_20}')