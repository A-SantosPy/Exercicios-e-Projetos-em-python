# indice de massa corporal
peso = float(input('Coloque seu peso(Kg): '))
altura = float(input('Coloque seu tamanho(m): '))
imc = peso / (altura * altura)
if imc:
    print('seu imc é \033[1;31m{:.1f}\033[m '.format(imc), end='')
    if imc < 18.5:
        print('você está abaixo do peso')
    elif imc < 24.9:
        print('seu peso está normal!')
    elif imc < 29.9:
        print('você está acima do peso!')
    elif imc < 39.9:
        print('você está com obesidade °1')
    elif imc > 40:
        print('você está com obesidade °2')
else:
    print('nao sei oq colocar aqui!')
