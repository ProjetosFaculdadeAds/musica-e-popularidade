from flask import Flask, render_template, request, jsonify
import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
from urllib.parse import parse_qs

# Configuração inicial
app = Flask(__name__)

# Carregar dados
df = pd.read_csv('dataset.csv')
df['duration_min'] = df['duration_ms'] / 60000

# Mapeamento de tonalidades
key_map = {
    -1: "Desconhecida", 0: "C", 1: "C#/Db", 2: "D", 3: "D#/Eb",
    4: "E", 5: "F", 6: "F#/Gb", 7: "G", 8: "G#/Ab", 9: "A", 10: "A#/Bb", 11: "B"
}
df['key_name'] = df['key'].map(key_map)

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    generos = sorted(df['track_genre'].unique())
    generos_selecionados = []
    musicas = []
    
    if request.method == 'POST':
        generos_selecionados = request.form.getlist('genero')
        if generos_selecionados:
            musicas = df[df['track_genre'].isin(generos_selecionados)]\
                      .sort_values('popularity', ascending=False)\
                      .head(10)\
                      .to_dict('records')
    
    return render_template(
        'index.html',
        generos_disponiveis=generos,
        generos_selecionados=generos_selecionados,
        musicas=musicas
    )

# Configuração do Dash
dash_app = Dash(
    __name__,
    server=app,
    url_base_pathname='/dash/',
    external_stylesheets=[dbc.themes.CYBORG]
)

dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='dash-container')
])

@callback(
    Output('dash-container', 'children'),
    Input('url', 'search')
)
def update_dash_container(search):
    params = parse_qs(search[1:] if search else '')
    generos = params.get('genero', ['pop', 'rock'])
    
    # Garantir que generos seja sempre uma lista
    if isinstance(generos, str):
        generos = [generos]
    
    return html.Div([
        dbc.Row([
            dbc.Col(dcc.Graph(id='bar-popularity'), md=6),
            dbc.Col(dcc.Graph(id='duration-vs-popularity'), md=6),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='bpm-vs-popularity'), md=6),
            dbc.Col(dcc.Graph(id='meter-vs-popularity'), md=6),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='key-distribution'), md=12),
        ])
    ])

@callback(
    Output('bar-popularity', 'figure'),
    Output('duration-vs-popularity', 'figure'),
    Output('bpm-vs-popularity', 'figure'),
    Output('meter-vs-popularity', 'figure'),
    Output('key-distribution', 'figure'),
    Input('url', 'search')
)
def update_graphs(search):
    params = parse_qs(search[1:] if search else '')
    generos = params.get('genero', ['pop', 'rock'])
    
    # Converter para lista se for string
    if isinstance(generos, str):
        generos = [g.strip() for g in generos.split(',')]
    
    filtered_df = df[df['track_genre'].isin(generos)]
    
    # Gráfico de popularidade
    bar_fig = px.bar(
        filtered_df.groupby('track_genre')['popularity'].mean().reset_index(),
        x='track_genre', y='popularity',
        title='Popularidade Média por Gênero',
        color='track_genre'
    )
    
    # Gráfico de duração
    duration_fig = px.box(
        filtered_df, x='track_genre', y='duration_min', color='track_genre',
        title='Duração (min) das Faixas por Gênero'
    )
    
    # Gráfico de BPM
    bpm_fig = px.histogram(
        filtered_df, x='tempo', nbins=30, color='track_genre',
        title='Distribuição de BPM por Gênero', barmode='overlay'
    )
    
    # Gráfico de compasso
    meter_fig = px.histogram(
        filtered_df, x='time_signature', color='track_genre',
        title='Distribuição de Compassos por Gênero', barmode='group'
    )
    
    # Gráfico de tonalidade
    key_fig = px.histogram(
        filtered_df, x='key_name', color='track_genre',
        title='Distribuição de Tonalidades por Gênero', barmode='group',
        category_orders={'key_name': list(key_map.values())}
    )
    
    return bar_fig, duration_fig, bpm_fig, meter_fig, key_fig

if __name__ == '__main__':
    app.run(debug=True)