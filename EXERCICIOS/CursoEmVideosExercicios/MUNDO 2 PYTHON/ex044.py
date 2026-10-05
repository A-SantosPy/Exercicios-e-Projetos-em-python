#Gerenciador de pagamentos

produ = float(input('Qual o valor do produto: '))
desc = int(input('Qual o desconto: '))
porc = (desc * desc) / 100
a = porc / produ
print('o valor do produto é {} e o desconto é de {}% ficando assim {}!'.format(produ, desc, a))

