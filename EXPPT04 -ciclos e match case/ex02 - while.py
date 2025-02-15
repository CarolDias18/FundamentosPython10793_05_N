'''
Aqui está o código em Python
para calcular a tabuada do 8 utilizando a instrução while, com comentários detalhados para explicar cada parte do processo:
'''

# Inicialização da variável que vai funcionar como contador
# Começamos com 1 porque a tabuada normalmente vai de 1 até 10
contador = 1

# Definimos o número para o qual queremos calcular a tabuada
numero = 8

# Imprimimos um cabeçalho para indicar que se trata da tabuada do 8
print("Tabuada do 8:")

# Ciclo while que irá repetir enquanto o contador for menor ou igual a 10
while contador <= 10:
    # Calcula o produto do número (8) pelo valor atual do contador
    resultado = numero * contador

    # Imprime o cálculo da tabuada no formato tradicional
    # Exemplo: 8 x 1 = 8, 8 x 2 = 16, etc.
    print(f"{numero} x {contador} = {resultado}")

    # Incrementa o contador para passar ao próximo número da tabuada
    contador += 1  # É o mesmo que escrever contador = contador + 1

# O ciclo termina automaticamente quando o contador ultrapassar 10