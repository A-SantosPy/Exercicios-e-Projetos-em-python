#kilometragem e multa

car = float(input('Qual a atual velocidade do carro: '))
km = (car - 80) * 7

if car > 80:
    print('Você está multado, pague R${:.2f}'.format(km))
else:
    print('Tenha uma boa viagem!')