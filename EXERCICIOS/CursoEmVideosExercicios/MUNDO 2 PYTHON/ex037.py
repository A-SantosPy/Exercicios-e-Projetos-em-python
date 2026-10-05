num = int(input('Coloque um número inteiro: '))
print('''
  \033[1;31m       TEMOS: \033[m
 \033[1;32mBinario     [1] EX: 01010 \033[m
 \033[1;33mOctal       [2] EX: o000 \033[m
 \033[1;34mHexadecimal [3] EX: 0B7A41 \033[m

''')

op = int(input('Qual sua opção: '))
if op == 1:
    print('seu número {} em BINARIO fica:\033[1;32m {}'.format(num, bin(num).upper()[2:]))
elif op == 2:
    print('seu número {} em OCTAL fica:\033[1;33m {}'.format(num, oct(num).upper()[2:]))
elif op == 3:
    print('seu número {} em HEXADECIMAL fica:\033[1;34m {}'.format(num, hex(num).upper()[2:]))
else:
    print('tente novamente com as opções acima!')