#crie um programa que leia o nome completo de uma pessoa é mostre:
#O nome com todas as letras maiusculas
#O nome com todas as letras minusculas
#quantas letras tem o primeiro nome
#quantas letras tem ao todo sem considerar espaço
n = input("Qual seu nome completo: ").strip()
s = n.split()
print("Seu nome em maiúsculas é {}".format(n.upper()))
print("Seu nome em minúsculas é {}".format(n.lower()))
print("Seu nome tem ao todo {} letras".format(len(n) - n.count(' ')))
print("Seu primeiro nome é {}, e ele tem {} letras".format(s[0], len(s[0])))
print('lele me ama')