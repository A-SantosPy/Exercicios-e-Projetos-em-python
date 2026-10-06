n = int(input('Quer ver a tabuada de qual valor: '))
while True:
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
    print('-' * 30)
    parar = str(input('PARA CONTINUAR: [S] '
    'PARA ENCERRAR: [N] ')).strip().upper()
    if parar == 'N':
        print('Programa encerrado.')
        break
    n = int(input('Quer ver a tabuada de qual valor: '))