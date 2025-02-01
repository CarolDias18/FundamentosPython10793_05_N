'''Escreva um programa que verifique se um determinado número introduzido pelo utilizador é nulo, positivo ou negativo.'''
# 1. Ler um número do utilizador
# 2. Verificar se o número é nulo, positivo ou negativo
# 3. Mostrar o resultado
n = int(input("Introduza um número: "))
if n > 0:
    print("O número é positivo.")
elif n < 0:
    print("O número é negativo.")
else:
    print("O número é nulo.")
    