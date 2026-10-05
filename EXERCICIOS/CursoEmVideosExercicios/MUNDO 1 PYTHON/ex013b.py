#Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
s = float(input('Qual seu salário? R$'))
print("Seu novo salário com 15% de aumento é R${:.2f} ".format(s + (s * 15) / 100))
