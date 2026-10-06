from random import randint

while True:
    jogador = int(input('Digite um valor entre 0 e 10: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')