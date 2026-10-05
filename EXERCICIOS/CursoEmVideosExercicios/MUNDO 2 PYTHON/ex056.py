#ultimo exercicio com FOR

somidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
mulher = 0
for p in range (1, 5):
    print('- - - - - {}° PESSOA - - - - -'.format(p))
    nome = str(input('NOME: ')).strip().upper()
    idade = int(input('IDADE: '))
    sex = str(input('SEXO [M/F]: ')).strip().upper()
    somidade += idade

    if p == 1 and sex in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sex in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sex in 'Ff' and idade < 20:
        sex = mulher
        mulher += 1


mediaidade = int(somidade / 4)
print('A media das idades é {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Tem {} mulher(s) menor(s) de 20 anos!'.format(mulher))