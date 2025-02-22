import pandas as pd

# Ler o ficheiro Excel (substituir 'nome_do_ficheiro.xlsx' pelo nome do seu ficheiro)
df = pd.read_excel('Teste.xlsx')

# Dicionário para armazenar os resultados por coluna


print(df)


resultados = {}

# Iterar por cada coluna do DataFrame
for coluna in df.columns:
    # Converter o conteúdo para string, remover as barras invertidas, converter para minúsculas e contar 'sr'
    total_sr = df[coluna].astype(str) \
                   .str.replace('\\', '', regex=False) \
                   .str.lower() \
                   .str.count('sr') \
                   .sum()
    resultados[coluna] = total_sr

# Exibir os resultados por coluna
for coluna, total in resultados.items():
    print(f"Coluna '{coluna}': {total} ocorrência(s) de 'sr'")
    
print(df)