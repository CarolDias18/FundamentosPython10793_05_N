'''Escreve um programa que solicite um número inteiro ao utilizador e caso o mesmo seja maior que 20, devolva o resultado da sua divisão por 2.'''

a=int(input("Insira um número inteiro:\n->"))

if a>=20:
    div=a/2
    print("A metade de %f é %f" %(a,div))

