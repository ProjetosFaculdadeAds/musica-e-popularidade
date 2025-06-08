from dash import html
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Dados fictícios
df = pd.DataFrame({
    'Gênero': ['Pop', 'Rock', 'Funk'],
    'Popularidade Média': [82, 75, 65]
})

fig = px.bar(df, x='Gênero', y='Popularidade Média', color='Gênero')

layout = html.Div([
    dcc.Graph(figure=fig)
])
