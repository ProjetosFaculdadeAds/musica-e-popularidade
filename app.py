import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Carregar o dataset
df = pd.read_csv('dataset.csv')

# Converter duração de ms para minutos
df['duration_min'] = df['duration_ms'] / 60000

# Inicializar o app
app = Dash(__name__)

# Layout do dashboard
app.layout = html.Div([
    html.H1("Análise de Faixas Populares no Spotify"),

    html.Label("Escolha os gêneros musicais:"),
    dcc.Dropdown(
        options=[{'label': g, 'value': g} for g in sorted(df['track_genre'].unique())],
        id='genre-selector',
        multi=True,
        value=['pop', 'rock']
    ),

    html.Br(),
    dcc.Graph(id='bar-popularity'),
    dcc.Graph(id='duration-vs-popularity'),
    dcc.Graph(id='bpm-vs-popularity'),
    dcc.Graph(id='meter-vs-popularity'),

    html.H2("Faixas que representam os padrões populares"),
    html.Div(id='recommended-tracks')
])

# Callback para atualizar todos os gráficos
@app.callback(
    Output('bar-popularity', 'figure'),
    Output('duration-vs-popularity', 'figure'),
    Output('bpm-vs-popularity', 'figure'),
    Output('meter-vs-popularity', 'figure'),
    Output('recommended-tracks', 'children'),
    Input('genre-selector', 'value')
)
def update_dashboard(selected_genres):
    filtered_df = df[df['track_genre'].isin(selected_genres)]

    # Gráfico de barras de popularidade média por gênero
    bar_fig = px.bar(filtered_df.groupby('track_genre')['popularity'].mean().reset_index(),
                     x='track_genre', y='popularity',
                     title='Popularidade Média por Gênero')

    # Gráfico de dispersão: duração vs popularidade
    duration_fig = px.box(filtered_df, x='track_genre', y='duration_min', color='track_genre',
                          points='all', title='Duração (min) das Faixas por Gênero')

    # Gráfico: BPM vs popularidade
    bpm_fig = px.histogram(filtered_df, x='tempo', nbins=30, color='track_genre', barmode='overlay',
                           title='Distribuição de BPM (Tempo) por Gênero')

    # Gráfico: Assinatura de compasso vs popularidade
    meter_fig = px.histogram(filtered_df, x='time_signature', color='track_genre', barmode='group',
                             title='Distribuição de Compassos por Gênero')

    # Encontrar padrões mais populares
    top_tracks = filtered_df.sort_values('popularity', ascending=False).head(10)
    track_list = html.Ul([
        html.Li(f"{row['track_name']} - {row['artists']} ({row['track_genre']})")
        for _, row in top_tracks.iterrows()
    ])

    return bar_fig, duration_fig, bpm_fig, meter_fig, track_list

# Executar o app
if __name__ == '__main__':
    app.run(debug=True)