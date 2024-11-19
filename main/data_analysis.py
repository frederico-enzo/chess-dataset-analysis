
import pandas as pd

# Carregar o arquivo enviado para inspecionar os dados
file_path = 'data/chess_games.csv'
chess_data = pd.read_csv(file_path)

# Identificar jogos inválidos ou incompletos
# Critérios: número de turnos <= 1 ou colunas críticas com valores inválidos
invalid_games = chess_data[
    (chess_data['turns'] <= 1) |
    (chess_data['moves'].str.strip() == "") |
    (chess_data['white_id'].str.strip() == "") |
    (chess_data['black_id'].str.strip() == "") |
    (chess_data['winner'].str.strip() == "")
]

# Remover jogos inválidos
cleaned_chess_data = chess_data.drop(index=invalid_games.index)

# Verificar quantos jogos foram removidos
removed_count = len(invalid_games)
remaining_count = len(cleaned_chess_data)

removed_count, remaining_count

# Exibir as primeiras linhas e informações gerais para entender a estrutura do dataset
chess_data.info(), chess_data.head()