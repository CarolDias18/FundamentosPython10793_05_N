
'''Elabora um programa para calcula a soma dos N primeiros números naturais (1+2+3+...+N) em 
que N é um número introduzido pelo utilizador '''


#Testa se o valor introduzido é um inteiro positivo usando a função isdigit(). Enquanto não for solicita constantemente ao

n = input("Introduza um número natural: ")
while True:
    try:
        n=int(n) 
        break
    except:
        print("O número introduzido não é válido")
        n = input("Introduza um número natural: ")
    
    

soma = 0
for i in range(1,n+1):
    soma = soma + i
print("soma = ", soma)


#Alternativa

n = "" #string vazia
while not n.lstrip('-').isdigit():
    n = input('Numero: ')

n = int(n)

#Alternativa
n = None    #valor nulo
while n is None:
    try:
        n = int(input('Numero: '))
    except:
        n = None


import re

n = ''
while not bool(re.fullmatch(r"-?\d+", n)):
    n = input('Numero: ')
    
n = int(n)
