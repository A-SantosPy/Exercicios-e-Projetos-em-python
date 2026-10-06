print('-' * 30)
print('{:^30}'.format('BANCO CEV'))
print('-' * 30)

valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
cedula_atual = 50
total_cedulas = 0

while True:
    # Se o valor restante for maior ou igual à cédula atual, subtrai e conta
    if total >= cedula_atual:
        total -= cedula_atual
        total_cedulas += 1
    else:
        # Se alguma cédula daquele valor foi emitida, mostra na tela
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R$ {cedula_atual}')
        
        # Rotaciona para a próxima cédula menor disponível
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        
        # Zera a contagem para a nova cédula
        total_cedulas = 0
        
        # Se o valor total chegou a zero, encerra o caixa eletrônico
        if total == 0:
            break

print('-' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
print('-' * 30)
