import dash
from dash import html, dcc

# --- 1️⃣ Création de l'application ---
app = dash.Dash(__name__)

# --- 2️⃣ Définition de la mise en page ---
app.layout = html.Div([
    html.H1(
        "Tableau de bord des statistiques de vente d'automobiles",
        style={'textAlign': 'center', 'color': '#1f77b4', 'margin-bottom': '30px'}
    ),

    # Dropdown 1 : sélectionner les statistiques
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
            value='total_sales',  # valeur par défaut
            clearable=False
        )
    ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px'}),

    # Dropdown 2 : saisir l'année (désactivé)
    html.Div([
        html.Label("Saisir l'année :"),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': str(i), 'value': i} for i in range(2000, 2024)],
            value=None,
            disabled=True  # dropdown désactivé
        )
    ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px'})
])

# --- 3️⃣ Lancer l'application ---
if __name__ == '__main__':
    app.run(debug=True)
