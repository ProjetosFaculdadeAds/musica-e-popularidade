from dash import html
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'Gênero': ['Pop'] * 4 + ['Funk'] * 4 + ['Eletrônica'] * 4,
    'BPM': [100, 105, 110, 108, 125, 128, 126, 130, 135, 138, 140, 145]
})

fig = px.box(df, x='Gênero', y='BPM',
             title='Distribuição de BPM por Gênero',
             template='plotly_dark',
             color_discrete_sequence=px.colors.qualitative.Dark24)

layout = html.Div([
    dcc.Graph(figure=fig)
])
