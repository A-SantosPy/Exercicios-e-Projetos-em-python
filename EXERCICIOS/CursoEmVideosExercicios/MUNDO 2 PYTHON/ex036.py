casa = float(input('-> PREÇO DA CASA DESEJADA: R$'))
salá = float(input('-> QUAL SEU SALÁRIO: R$'))
ano = int(input('-> COLOQUE O FINANCIAMENTO: '))
m = (salá*30) / 100
pr = casa / (ano * 12)
print('para pagar a casa no valor de R${:.2f} em {:.2f} anos'.format(casa, ano), end='')
print(' a pretação será de R${:.2f}'.format(pr))

if pr <= m:
    print('O EMPRÉSTIMO pode ser feito com SUCESSO!')
elif pr > m:
    print('NÃO foi possivel efetuar o EMPRÉSTIMO!')
