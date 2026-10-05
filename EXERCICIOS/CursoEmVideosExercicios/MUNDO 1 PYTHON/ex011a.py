#crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta nescessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²
l = float(input("Qual a largura da parede? "))
a = float(input("Qual a altura dessa parede? "))
mq = l * a
t = mq / 2
print("Sua parede tem a dimenão de {} x {} e sua área é de {:.3f}m².".format(l, a, mq))
print("Para pintar essa parede, você vai precisar de {:.3f}l de tinta.".format(t))
