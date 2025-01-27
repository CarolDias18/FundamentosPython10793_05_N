'''Programa que recebe três parâmetros inteiros (horas, minutos e segundos) e converte para segundos'''
# Passo 1, 2 e 3: solicitar horas, minutos e segundos
horas = input("Digite as horas: ")
minutos = input("Digite os minutos: ")
segundos = input("Digite os segundos: ")

# Passo 4: converter para inteiro
horas = int(horas)
minutos = int(minutos)
segundos = int(segundos)

# Passo 5: calcular total em segundos
total_segundos = (horas * 3600) + (minutos * 60) + segundos

# Passo 6: exibir resultado
print("O total em segundos é:", total_segundos)