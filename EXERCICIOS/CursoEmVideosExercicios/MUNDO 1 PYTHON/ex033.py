# ler 3 numeros maior pro menor


a = int(input('Coloque um número: '))
b = int(input('Outro número: '))
c = int(input('+ 1 número: '))
# verificando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor número é {}'.format(menor))
# verificando o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior deles é {}'.format(maior))
