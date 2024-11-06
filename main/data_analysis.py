# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Carregando o dataset (substitua 'caminho_do_arquivo.csv' pelo caminho do seu arquivo)
df = pd.read_csv('caminho_do_arquivo.csv')

# Exibindo as primeiras linhas do dataset para uma visualização inicial
print(df.head())

# Realizando uma análise básica, como verificar informações sobre o dataset
print(df.info())
print(df.describe())

# Criando um gráfico de exemplo
# Alterar a coluna para algo que exista no seu dataset, como 'idade' ou 'salário', por exemplo
df['coluna_exemplo'].hist(bins=20, color='skyblue')
plt.title('Distribuição da Coluna Exemplo')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.show()
