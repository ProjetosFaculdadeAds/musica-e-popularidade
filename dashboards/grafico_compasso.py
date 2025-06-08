from dash import html
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame({
    'Compasso': ['4/4', '3/4', '6/8'],
    'Frequência': [85, 10, 5]
})

fig = go.Figure(data=[
    go.Pie(labels=df['Compasso'], values=df['Frequência'], hole=0.5)
])

fig.update_layout(title='Distribuição de Compasso',
                  template='plotly_dark')

layout = html.Div([
    dcc.Graph(figure=fig)
])
