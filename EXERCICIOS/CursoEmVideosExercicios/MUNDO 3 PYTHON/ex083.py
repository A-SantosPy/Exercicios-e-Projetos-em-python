#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

# Lê a expressão digitada pelo usuário
expr = str(input('Digite a expressão: '))

# Cria uma lista que funcionará como uma pilha
pilha = []

# Percorre cada caractere da expressão
for simb in expr:
  if simb == '(':
    pilha.append('(')
  elif simb == ')':
    if len(pilha) > 0:
      pilha.pop()  # Remove o último '(' correspondente
    else:
      pilha.append(')')  # Encontrou ')' a mais e interrompe
      break

# Verifica se a pilha ficou vazia (expressão válida)
if len(pilha) == 0:
  print('Sua expressão está válida!')
else:
  print('Sua expressão está errada!')
