'''Programa que recebe os catetos de um triângulo retângulo e devolve o valor da hipotenusa'''

# Passo 1 e 2: solicitar valores de a e b
a = input("Digite o valor do cateto a: ")
b = input("Digite o valor do cateto b: ")

# Passo 3: converter para float (caso haja decimais)
a = float(a)
b = float(b)

# Passo 4: calcular a^2 + b^2
soma_quadrados = a**2 + b**2

# Passo 5: tirar a raiz quadrada
hipotenusa = soma_quadrados ** 0.5

# Passo 6: exibir resultado
print("O valor da hipotenusa é:", hipotenusa)