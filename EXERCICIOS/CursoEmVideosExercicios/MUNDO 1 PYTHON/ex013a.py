#Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
s = float(input("Qual seu salário? R$"))
a = s + (s * 15) / 100
print("Seu novo salário será R${:.2f}, pois recebeu 15% de aumento. Parábens!".format(a))