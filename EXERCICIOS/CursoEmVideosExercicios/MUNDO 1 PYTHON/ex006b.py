#crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
n = int(input("coloque um número: "))
d = n*2
t = n*3
rq = n**0.5
print("o dobro do número escolhido é {} o terço é {} e a raiz quadrada é {:.3f}".format(d, t, rq))