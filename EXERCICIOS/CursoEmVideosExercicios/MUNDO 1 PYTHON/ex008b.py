#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
m = float(input("coloque um valor em metros: "))
print("{:.0f}m é {:.1f}km, {:.0f}hm, {:.0f}dm, {:.0f}cm, {:.0f}mm".format(m, m/1000, m/100, m/10, m*100, m*1000))
