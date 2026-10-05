#triangulos
r1 = float(input('1° reta: '))
r2 = float(input('2° reta: '))
r3 = float(input('3° reta: '))
print('A primeira reta é {:.0f}, a segunda é {:.0f}, e a terceira é {:.0f}!'.format(r1, r2, r3))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('da pra formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('NÃO da pra FORMAR um TRIÂNGULO')