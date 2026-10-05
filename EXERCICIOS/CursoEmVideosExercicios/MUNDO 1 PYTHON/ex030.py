#par ou impar

num = int(input('Coloque um número: '))
resu = num % 2

if resu == 0:
    print('{} é par!'.format(num))
else:
    print('{} é ímpar!'.format(num))