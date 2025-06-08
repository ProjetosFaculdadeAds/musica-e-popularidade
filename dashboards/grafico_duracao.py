from dash import html
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'Gênero': ['Pop', 'Rock', 'Funk', 'Eletrônica', 'Hip-Hop'],
    'Duração (minutos)': [3.2, 3.8, 2.5, 4.1, 3.0]
})

fig = px.bar(df, x='Gênero', y='Duração (minutos)', color='Gênero',
             title='Duração Média por Gênero',
             template='plotly_dark',
             color_discrete_sequence=px.colors.qualitative.Dark24)

layout = html.Div([
    dcc.Graph(figure=fig)
])
