#crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome
nome = str(input("Qual seu nome completo? ")).strip()
print('seu nome tem silva? {}'.format('SILVA' in nome.upper()))