#pip install pandas
#pip install openpyxl # para carregar ficheiros xlsx
import pandas as pd
filename_in = 'Teste.xlsx'
filename_out = filename_in.replace('.xlsx', '_clean.xlsx')
df = pd.read_excel(filename_in)
# limpar as todas barras em todas as colunas
for col in df.columns:
    for i, value in enumerate(df[col]):
        if isinstance(value, str):  # a função de replace funciona apenas em strings
            df[col][i] = value.replace('\\', '')
print(df.head())
df.to_excel(filename_out, index=False)