'''Escreve um programa que utilize a instrução while para calcular e apresentar as tabuadas dos números de 1 a 10.
O programa deve exibir, para cada número, a sua tabuada completa desde a multiplicação por 1 até à multiplicação por 10.'''

# Inicialização da variável que representa o número da tabuada atual
# Começamos com 1 porque queremos as tabuadas de 1 até 10
numero = 1

# Ciclo while externo para percorrer as tabuadas de 1 até 10
while numero <= 10:
    # Imprime um cabeçalho para indicar qual tabuada está a ser calculada
    print(f"Tabuada do {numero}:")
    
    # Inicialização do contador para a multiplicação de 1 até 10
    contador = 1  # O contador vai de 1 até 10 para cada número
    
    # Ciclo while interno para calcular a tabuada do número atual
    while contador <= 10:
        # Calcula o produto do número atual pelo contador
        resultado = numero * contador  # Exemplo: 2 * 3 = 6
        
        # Imprime o resultado da multiplicação no formato tradicional
        # O uso do f-string facilita a formatação da saída
        print(f"{numero} x {contador} = {resultado}")
        
        # Incrementa o contador para a próxima multiplicação
        contador += 1  # Isto faz com que o ciclo continue até contador ser maior que 10

    # Linha em branco para separar visualmente as tabuadas
    print()  # Apenas para melhorar a legibilidade do resultado no ecrã

    # Incrementa o número para passar para a próxima tabuada
    numero += 1  # Após terminar uma tabuada, avançamos para o próximo número
    
