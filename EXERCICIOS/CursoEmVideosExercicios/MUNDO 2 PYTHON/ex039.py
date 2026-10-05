from datetime import date
atual = date.today().year
n = str(input('Coloque seu nome: '))
nas = int(input('Qual seu ano de nascimento: '))
idade = atual - nas

print('{} você nasceu em {} e tem ou vai ter {} anos em {}!'.format(n, nas, idade, atual))

if idade == 18:
    saldo = idade - 18
    print('você tem que se alistar agora!')
elif idade < 18:
    saldo = idade - 18
    print('ainda esta cedo pra se alistar')
    ano = saldo + atual
    print('seu alistamento ocorrerá em {} anos'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = saldo + atual
    print('Você deveria ter se alistado há {} anos'.format(saldo))