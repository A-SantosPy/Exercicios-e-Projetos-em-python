#ex palindromo:
frase = str(input('Coloque uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range (len(junto)-1, -1, -1):
    inverso += junto [letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
        print('{} é um palindromo!'.format(frase))
else:
        print('Está frase não é um palindromo!')