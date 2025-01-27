'''Programa que recebe a distância percorrida (em km) e a quantidade de combustível gasto (em litros), calcula o consumo em km/l e mostra uma mensagem de acordo com o resultado'''

# Passo 1 e 2: solicitar distância e combustível
distancia = input("Digite a distância percorrida (km): ")
combustivel = input("Digite a quantidade de combustível gasto (litros): ")

# Passo 3: converter para float
distancia = float(distancia)
combustivel = float(combustivel)

# Passo 4: calcular consumo (km/l)
consumo = distancia / combustivel

# Passo 5: mostrar mensagem de acordo com o consumo
print("O consumo médio do carro é:", consumo, "km/l")

if consumo < 8:
    print("Consumo elevado (pouco económico).")
elif consumo < 12:
    print("Consumo razoável.")
else:
    print("Consumo bom (carro económico).")