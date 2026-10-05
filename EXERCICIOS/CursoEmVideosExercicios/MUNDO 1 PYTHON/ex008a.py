#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
m = float(input('Coloque um valor em metros: '))
km = m /1000
hm = m /100
dm = m/10
cm = m * 100
mm = m * 1000
print('{}m é {:.0f}km, {:.0f}hm, {:.0f}dm, {:.0f}cm e {:.0f}mm '.format(m, km, hm, dm, cm, mm))
