#progressão aritimetica

print(20*'=')
print('10 TERMOS DE UM P.A:')
print(20*'=')

#variaveis
num = int(input('Primeiro termo: '))
razao = int(input('razão: '))
decimo = num + (10 - 1) * razao

#laço de repetição
for c in range(num, decimo + razao, razao):
    print(c, end='-> ')

print('ACABOU!')
