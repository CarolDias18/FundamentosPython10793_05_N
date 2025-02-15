for i in range(1, 11):  # Loop externo (de 1 a 10)
    # Loop interno (para cada valor de i, j varia de 1 a 10)
    for j in range(1, 11):
        multiplicacao = i * j  # Calcula a multiplicação de i por j
        
        print("%d*%d=%d\n"%(i,j,multiplicacao))  # Imprime o resultado 
           
        print("{}*{}={}\n".format(i,j,multiplicacao))      
                
        print(f"{i}*{j}={multiplicacao}\n")
        
        # Imprime o resultado

print("concluido")  # Indica que o processo foi concluído
