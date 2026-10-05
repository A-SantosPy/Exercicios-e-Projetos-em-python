#crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta nescessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²
l = float(input('quanto de largura tem a parede? '))
a = float(input('quanto de altura tem a parede? '))
print("As medias dessa parede é de {} x {}. A área é {:.3f}m², e você irá precisar de {:.3f}l de tinta pra pinta-la.".format(l, a, l*a,(l*a)/2))



