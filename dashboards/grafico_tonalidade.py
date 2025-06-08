from dash import html
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'Gênero': ['Pop', 'Rock', 'Funk', 'Pop', 'Rock', 'Funk'],
    'Tonalidade': ['C', 'D', 'A', 'G', 'C#', 'F']
})

fig = px.histogram(df, x='Tonalidade', color='Gênero',
                   barmode='group',
                   title='Distribuição de Tonalidade por Gênero',
                   template='plotly_dark',
                   color_discrete_sequence=px.colors.qualitative.Dark24)

layout = html.Div([
    dcc.Graph(figure=fig)
])
