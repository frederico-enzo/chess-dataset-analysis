
import pandas as pd

# Carregar o arquivo enviado para inspecionar os dados
file_path = 'data/chess_games.csv'
chess_data = pd.read_csv(file_path)

# Exibir as primeiras linhas e informações gerais para entender a estrutura do dataset
chess_data.info(), chess_data.head()

# Identificar jogos inválidos ou incompletos
# Critérios: número de turnos <= 1 ou colunas críticas com valores inválidos
invalid_games = chess_data[
    (chess_data['turns'] <= 1) |
    (chess_data['moves'].str.strip() == "") |
    (chess_data['white_id'].str.strip() == "") |
    (chess_data['black_id'].str.strip() == "") |
    (chess_data['winner'].str.strip() == "")
]

