'''Escreve um programa que calcule a soma dos 10 primeiros números inteiros positivos 
e devolva o resultado para o ecrã.'''


# Inicialização das variáveis

numero = 1
soma = 0
# Ciclo while para somar os 10 primeiros números inteiros positivos
while numero <= 10:
    soma =soma + numero
    print(soma)
    numero = numero + 1

# Exibição do resultado no ecrã
print("A soma dos 10 primeiros números inteiros positivos é:", soma)


#operadores de atribuição : = , += , *= , -= , /=, %=

# numero += 2    é igual a numero = numero+2
# numero *= 2    é igual a numero = numero*2
# numero -= 2    é igual a numero = numero-2
# numero /= 2    é igual a numero = numero/2
# numero %= 2    é igual a numero = numero%2