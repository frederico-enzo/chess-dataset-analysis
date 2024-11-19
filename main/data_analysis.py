import pandas as pd
import matplotlib.pyplot as plt

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

# Remover jogos inválidos
cleaned_chess_data = chess_data.drop(index=invalid_games.index)

# Verificar quantos jogos foram removidos
removed_count = len(invalid_games)
remaining_count = len(cleaned_chess_data)

removed_count, remaining_count

# Analisar desempenho dos jogadores brancos
white_stats = (
    cleaned_chess_data.groupby('white_id')
    .agg(
        total_games=('game_id', 'count'),
        victories=('winner', lambda x: (x == 'White').sum()),
        average_rating=('white_rating', 'mean')
    )
    .assign(win_rate=lambda df: df['victories'] / df['total_games'])
    .reset_index()
    .rename(columns={'white_id': 'player_id'})
)

# Analisar desempenho dos jogadores negros
black_stats = (
    cleaned_chess_data.groupby('black_id')
    .agg(
        total_games=('game_id', 'count'),
        victories=('winner', lambda x: (x == 'Black').sum()),
        average_rating=('black_rating', 'mean')
    )
    .assign(win_rate=lambda df: df['victories'] / df['total_games'])
    .reset_index()
    .rename(columns={'black_id': 'player_id'})
)

# Combinar estatísticas para um panorama geral
player_stats = (
    pd.concat([white_stats, black_stats])
    .groupby('player_id')
    .agg(
        total_games=('total_games', 'sum'),
        victories=('victories', 'sum'),
        average_rating=('average_rating', 'mean'),
        win_rate=('win_rate', 'mean')
    )
    .sort_values(by='win_rate', ascending=False)
    .reset_index()
)

# Exibir as 5 melhores estatísticas
player_stats.head()


# Criar um gráfico da distribuição da taxa de vitória
plt.figure(figsize=(10, 6))
plt.hist(player_stats['win_rate'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribuição da Taxa de Vitória dos Jogadores', fontsize=14)
plt.xlabel('Taxa de Vitória (Win Rate)', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Salvar o gráfico como imagem
output_path = 'data/win_rate_distribution.png'
plt.savefig(output_path)
plt.close()

output_path