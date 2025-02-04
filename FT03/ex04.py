'''Escreve um programa que receba dois números reais e indique qual o maior dos dois números. Considera a possibilidade de o utilizador indicar dois números iguais.'''

# Recebendo dois números reais
num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))
# Comparando os dois números
if num1 > num2:
    print(f"O maior número é {num1}")
elif num2 > num1:
    print(f"O maior número é {num2}")
else:
    print("Os dois números são iguais")
    
#ou

num1 = input('Num 1: ')
num2 = input('Num 2: ')

num1, num2 = int(num1), int(num2)

if num1 == num2:
    print(f'Os números são igual')
else:
    maior = max(num1, num2)
    print(f'O número {maior} é maior')
