#desenvolver o comprimento de 3 retas e se pode ou não formar um triangulo
import emoji
print('--- ESTE É UM ANALISADOR DE TRIÂNGULOS ---')

ra = float(input('Comprimento da 1° reta: '))
rb = float(input('Comprimento da 2° reta: '))
rc = float(input('Comprimento da 3° reta: '))

if ra < rb + rc and rb < ra + rc and rc < ra + rb:
    print(emoji.emojize('Deu bom, dá pra formar um triângulo! :thumbs_up:'))
else:
    print(emoji.emojize('Deu ruim, não dá pra formar um triângulo! :thumbs_down:'))