'''Escreve um programa que solicite um número inteiro ao utilizador e verifique se o mesmo é par ou ímpar. A mensagem no ecrã deverá ter o seguinte formato;
"O número [número] é [par/ímpar]"Escreve um programa que solicite um número inteiro ao utilizador e verifique se o mesmo é par ou ímpar. A mensagem no ecrã deverá ter o seguinte formato;
"O número [número] é [par/ímpar]"'''

while True:
    try:
        numero = int(input("Por favor, insira um número: "))
    except:
        print("O valor inserido não é um número inteiro")
       
    
      
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
    
    
    
    