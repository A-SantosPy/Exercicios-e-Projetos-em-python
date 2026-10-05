''' for f in range(1, 51):
    n = str(input('coloque seu nome: ')).strip().upper()
    print('{} você é o número {}'.format(n,f))
print('FIM') '''
from os import close

'''p = 1
while p != 50:
    print('você é o número {}'.format(p))
    p = p + 1
print('FIM')'''

'''r = 'S'
while r == 'S':
    n = int(input('coloque um número: '))
    r = str(input('Você quer continuar: [S/N]')).upper()
print('FIM')
'''

'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você teve {} números pares e {} números impares!'.format(par, impar))
print('FIM')'''

sexo = str(input('COLOQUE SEU SEXO: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados incorretos, Tente novamente: ')).strip().upper()[0]
print('SEXO {} REGISTRADO!'.format(sexo))
print('FIM!')