'''Programa que calcula o volume de uma esfera'''
# Passo 1: solicitar valor do raio
raio = input("Digite o valor do raio da esfera: ")

# Passo 2: converter para float
raio = float(raio)

# Passo 3: definir pi
pi = 3.14159

# Passo 4: calcular volume
volume = (4.0/3.0) * pi * (raio**3)

# Passo 5: exibir resultado
print("O volume da esfera é:", volume)