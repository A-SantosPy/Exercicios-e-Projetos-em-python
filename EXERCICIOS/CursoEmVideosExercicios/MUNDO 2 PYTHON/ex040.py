#media
p1 = float(input('Coloque sua primeira nota: '))
p2 = float(input('Coloque sua segunda nota: '))
med = (p1 + p2) / 2
if med < 5:
    print('\033[1;31mVocê está reprovado!')
elif med >= 5 and med < 7 :
    print('\033[1;33mvocê esta de recuperação!')
else:
    print('\033[1;32mVocê foi aprovado!\033[m \033[1;31m não fez + que sua obrigação\033[m')
