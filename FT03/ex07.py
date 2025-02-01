'''Elabora um programa para verificar se um ano é bissexto ou não. A condição para ser um ano bissexto é: o ano deve ser divisível por 400; ou se for divisível por 4 e não for divisível por 100'''

ano = int(print("Introduza um ano:"))

if ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
elif ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano {ano} é bissexto')
    
   