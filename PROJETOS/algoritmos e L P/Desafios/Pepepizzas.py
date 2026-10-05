# projeto de atendimento automatizado de pizzaria
# nesse projeto deve conter:
# 1 Tamanho da pizza
# 2 Recheio da pizza
# 3 Borda da pizza
# 4 Extras da pizza
# 5 Forma de consumo (se vai ser local ou pra viagem )

print('\033[30;5m~\033[m'* 50)
print('Bem vindo a \033[32m PEPEPIZZAS \033[m, o codigo do\033[32m sabor \033[m!')
print('\033[30;5m~\033[m'* 50)
print('Veja o Cardapio a baixo: ')
print("""
\033[1;30m==================================================\033[m
              \033[1;33m🍕 CARDAPIO PEPEPIZZAS 🍕\033[m
\033[1;30m==================================================\033[m

\033[1;35m1.\033[m Tamanho da Pizza
   [P] Pequena  ....................... \033[1;32mR$ 25,00\033[m
   [M] Média    ....................... \033[1;32mR$ 35,00\033[m
   [G] Grande   ....................... \033[1;32mR$ 45,00\033[m

\033[1;35m2.\033[m Recheio
   Mussarela ...................... \033[1;32mR$  0,00\033[m
   Pepperoni ...................... \033[1;32mR$  7,00\033[m
   Da Casa   ...................... \033[1;32mR$ 10,00\033[m

\033[1;35m3.\033[m Borda
   Sem Cheddar .................... \033[1;32mR$  0,00\033[m
   Com Cheddar .................... \033[1;32mR$  5,00\033[m

\033[1;35m4.\033[m Toppings Extras (Escolha até 4)
   • Alho        ...................... \033[1;32mR$  2,00\033[m
   • Cebola      ...................... \033[1;32mR$  2,00\033[m
   • Milho       ...................... \033[1;32mR$  3,00\033[m
   • Azeitona    ...................... \033[1;32mR$  3,00\033[m

\033[1;34m5.\033[m Tipo de Consumo
   Comer no local (Opcional: \033[1;32m+10%\033[m de gorjeta)
   Levar para casa (Ganhe \033[1;32m5%\033[m de desconto!)

\033[1;30m==================================================\033[m
""")

print('AGORA VAMOS MONTAR SUA PIZZA! ')
#variavel que vai ser usada para contabilizar tudo no final
valor_total = 0
sub_total = 0
#NUMERO 1 : TAMANHO DA PIZZA =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#variavel do tamanho da pizza e o subtotal para contabilizar o valor no final do codigo
tamanho_da_pizza = ''

while tamanho_da_pizza not in ['P', 'M', 'G']:
    tamanho_da_pizza = str(input('SELECIONE O TAMANHO DESEJADO [P, M, G]: ')).upper().strip()
    if tamanho_da_pizza == 'P':
        print("TAMANHO \033[1;31mP\033[m SELECIONADO")
        sub_total += 25
        valor_total = sub_total
    elif tamanho_da_pizza == 'M':
        print("TAMANHO \033[1;31mM\033[m SELECIONADO")
        sub_total += 35
        valor_total = sub_total
    elif tamanho_da_pizza == 'G':
        print("TAMANHO \033[1;31mG\033[m SELECIONADO")
        sub_total += 45
        valor_total = sub_total
    else:
        print('\033[31mOpção inválida! Digite apenas P, M ou G.\033[m')
print(f'O VALOR ATUAL DA SUA PIZZA É \033[32mR${sub_total:.2f}\033[m')
print('\033[30;5m~\033[m'* 50)

#NUMERO 2 : SABOR DA PIZZA =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print('SELECIONE O SABOR DA PIZZA: ')
print('[1] - mussarela '
      '[2] - peperoni '
      '[3] - A moda da casa')

sabor_pizza = 0
sabor_nome = ""
while sabor_pizza not in [1, 2, 3]:
    sabor_pizza = int(input('DIGITE O SABOR DESEJADO: '))

    if sabor_pizza == 1:
        sabor_nome = 'MUSSARELA'
        sub_total += 0
    elif sabor_pizza == 2:
        sabor_nome = 'PEPERONI'
        sub_total += 7
    elif sabor_pizza == 3:
        sabor_nome = 'A MODA DA CASA'
        sub_total += 10
    else:
        print('\033[31mOpção inválida! Digite apenas 1, 2 ou 3.\033[m')
print(f'O SABOR SELECIONADO FOI \033[31m{sabor_nome}!\033[m')
print(f'O VALOR ATUAL DA SUA PIZZA É \033[32mR${sub_total:.2f}\033[m')
print('\033[30;5m~\033[m'* 50)

# NUMERO 3: BORDA DA PIZZA =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print('SELECIONE A BORDA DA PIZZA [S/N]: ')
borda_pizza = ''
while borda_pizza not in ["S","N"]:
    borda_pizza = str(input('DESEJA ADICIONAR \033[1;33mCHEDDAR\033[m NA BORDA DA PIZZA [S/N]: ')).upper().strip()
    if borda_pizza == 'N':
        print('OPÇÃO \033[1;31mN\033[m SELECIONADA, BORDA NAO ADICIONADA!')
        sub_total += 0
    elif borda_pizza == 'S':
        print('OPÇÃO \033[1;32mS\033[m SELECIONADA, BORDA DE \033[1;33mCHEDDAR\033[m ADICIONADA!')
        sub_total += 5
    else:
        print('\033[31mOpção inválida! Digite apenas S ou N.\033[m')
print(f'O VALOR ATUAL DA SUA PIZZA É \033[32mR${sub_total:.2f}\033[m')
print('\033[30;5m~\033[m'* 50)

# NUMERO 4: EXTRA NA PIZZA =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
extra_na_pizza = 0
quantidade_extra = 0
extra_nome = ''
confirmacao = ''
lista = []
print('[1] - ALHO [2] - CEBOLA [3] - MILHO [4] - AZEITONA')

while quantidade_extra < 4:
    extra_na_pizza = 0
    # Pergunta se o cliente quer mesmo um extra antes de obrigá-lo a escolher 4
    deseja_extra = input('Deseja adicionar um ingrediente extra? [S/N]: ').strip().upper()
    if deseja_extra == 'N':
        break
    elif deseja_extra != 'S':
        print('\033[31mOpção inválida! Digite apenas S ou N.\033[m')
        continue

    while extra_na_pizza not in [1, 2, 3, 4]:
        extra_na_pizza = int(input('SELECIONE O EXTRA NA PIZZA: '))

        if extra_na_pizza == 1:
            lista.append('ALHO')
            sub_total += 2

        elif extra_na_pizza == 2:
            lista.append('CEBOLA')
            sub_total += 2

        elif extra_na_pizza == 3:
            lista.append('MILHO')
            sub_total += 3

        elif extra_na_pizza == 4:
            lista.append('AZEITONA')
            sub_total += 3
        else:
            print('\033[31mOpção inválida! Digite apenas 1, 2, 3 ou 4.\033[m')

    quantidade_extra += 1
    print(f'\033[1;32m{extra_nome}\033[m adicionado com sucesso!')

    if quantidade_extra == 4:
        print('\033[1;33mVocê atingiu o limite máximo de 4 extras!\033[m')


print(f'O VALOR ATUAL DA SUA PIZZA É \033[32mR${sub_total:.2f}\033[m')
print('\033[30;5m~\033[m'* 50)

# NUMERO 5: DESCONTO AUTOMATICO =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

comer_no_local = 0

print('[1] - COMER NO LOCAL [2] - LEVAR PARA A VIAGEM')

while comer_no_local not in [1 or 2]:
    comer_no_local = int(input('DIGITE A OPÇÃO DESEJADA: '))

    if comer_no_local == 1:
        pergunta = str(input('DESEJA ADICIONAR 10% DE GORJETA AO GARÇON [S/N]:')).upper().strip()
        if pergunta == 'S':
            sub_total *= 1.10
            print(f'O SUBTOTAL FICA \033[32mR${sub_total:.2f}\033[m')
            gorgeta = comer_no_local
            comer_no_local = 'GORGETA'
            break

        elif pergunta == 'N':
            valor_total = sub_total
            print('NÃO OUVE GORGETA!')
            break

    elif comer_no_local == 2:
        sub_total *= 0.95
        print('O DESCONTO DE 5% FOI ADCIONADO COM SUCESSO!')
        print(f'O SUBTOTAL FICA \033[32mR${sub_total:.2f}\033[m')
        desconto = comer_no_local
        comer_no_local = 'DESCONTO'
        break

    else:
        print('\033[31mOpção inválida! Digite apenas 1 ou 2.\033[m')
        break

valor_total = sub_total

print('\033[30;5m~\033[m'* 50)
print('SUA PIZZA FICOU MONTADA ASSIM: ')
print(f'TAMANHO:{tamanho_da_pizza} RECHEIO:{sabor_nome} BORDA:{borda_pizza}')
print(f"Os itens extras adicionados foram: {', '.join(lista).strip()}")
print(f'O CLIENTE OPTOU POR {comer_no_local}')
print(f'O TOTAL FOI DE R${valor_total:.2f}')


print('\033[30;5m~\033[m'* 50)
print('Volte sempre a\033[32m PEPEPIZZAS\033[m, não esqueça o codigo do\033[32m sabor \033[m!')
print('\033[30;5m~\033[m'* 50)