
import pandas as pd

# Carregar o arquivo enviado para inspecionar os dados
file_path = 'data/chess_games.csv'
chess_data = pd.read_csv(file_path)

# Exibir as primeiras linhas e informações gerais para entender a estrutura do dataset
chess_data.info(), chess_data.head()