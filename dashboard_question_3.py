import dash
from dash import html, dcc

# --- Création de l'application ---
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Tableau de bord des statistiques de vente d'automobiles",
        style={'textAlign': 'center', 'color': '#1f77b4', 'margin-bottom': '30px'}
    ),

    # Dropdown pour sélectionner les statistiques
    html.Div([
        html.Label("Sélectionner les statistiques :"),
        dcc.Dropdown(
            id='stats-dropdown',
            options=[
                {'label': 'Ventes totales', 'value': 'total_sales'},
                {'label': 'Dépenses publicitaires', 'value': 'ad_exp'},
                {'label': 'PIB', 'value': 'gdp'},
                {'label': 'Taux de chômage', 'value': 'unemployment'}
            ],
            value='total_sales',
            clearable=False
        )
    ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px'}),


    html.Div([
        html.Label("Saisir l'année :"),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': str(i), 'value': i} for i in range(2000, 2024)],
            value=None,
            disabled=True
        )
    ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px'}),

    html.Div(
        id='output-container',
        className='output-container', 
        children="Ici apparaîtront les résultats ou graphiques sélectionnés.",
        style={'marginTop': '20px', 'padding': '15px', 'border': '1px solid #ccc'}
    )
])

if __name__ == '__main__':
    app.run(debug=True)
