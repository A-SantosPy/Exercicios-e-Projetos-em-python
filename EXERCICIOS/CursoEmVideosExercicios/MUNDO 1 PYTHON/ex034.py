# salario aumento

salario = float(input('Qual seu sálario: R$'))

if salario <= 1250:
    porcentagem = (salario * 15) / 100 + salario
    print('Seu salario de R${:.2f} ficou R${:.2f}'.format(salario, porcentagem))
if salario > 1250:
    porcentagem = (salario * 10) / 100 + salario
    print('Seu salario de R${:.2f} ficou R${:.2f}'.format(salario, porcentagem))


#if salario <= 1250:
#   novo = salario + (salario*15 / 100)
#   print('seu salario de R${} fica R${} com 15% de aumento'.format(salario, novo))
#else:
#   novo = salario + (salario * 10 / 100)
#   print('seu salario de R${} fica R${} com 10% de aumento'.format(salario, novo))
