import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# ---  Charger les données ---
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv'
df = pd.read_csv(url)

# ---  Filtrer uniquement la période de récession ---
df_recession = df[df['Recession'] == 1]

# ---  Créer l'application ---
app = dash.Dash(__name__)

# ---  Mise en page avec 2 lignes x 2 colonnes ---
app.layout = html.Div([
    html.H1(
        "Statistiques de ventes pendant les périodes de récession",
        style={'textAlign': 'center', 'color': '#1f77b4', 'margin-bottom': '30px'}
    ),

    html.Div([
        # Ligne 1, Colonne 1 : Ventes annuelles par type de véhicule (ligne)
        html.Div([
            dcc.Graph(
                figure=px.line(
                    df_recession.groupby(['Year','Vehicle_Type'], as_index=False)['Automobile_Sales'].sum(),
                    x='Year', y='Automobile_Sales', color='Vehicle_Type',
                    markers=True,
                    title='Ventes annuelles par type de véhicule'
                )
            )
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),

        # Ligne 1, Colonne 2 : Évolution du PIB (ligne)
        html.Div([
            dcc.Graph(
                figure=px.line(
                    df_recession.groupby('Year', as_index=False)['GDP'].mean(),
                    x='Year', y='GDP',
                    markers=True,
                    title='Évolution du PIB moyen'
                )
            )
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),
    ]),

    html.Div([
        # Ligne 2, Colonne 1 : Ventes totales par type de véhicule (barre)
        html.Div([
            dcc.Graph(
                figure=px.bar(
                    df_recession.groupby('Vehicle_Type', as_index=False)['Automobile_Sales'].sum(),
                    x='Vehicle_Type', y='Automobile_Sales',
                    title='Ventes totales par type de véhicule'
                )
            )
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),

        # Ligne 2, Colonne 2 : Dépenses publicitaires par type de véhicule (camembert)
        html.Div([
            dcc.Graph(
                figure=px.pie(
                    df_recession.groupby('Vehicle_Type', as_index=False)['Advertising_Expenditure'].sum(),
                    names='Vehicle_Type', values='Advertising_Expenditure',
                    title='Répartition des dépenses publicitaires'
                )
            )
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),
    ])
])

# ---  Lancer l'application ---
if __name__ == '__main__':
    app.run(debug=True)

