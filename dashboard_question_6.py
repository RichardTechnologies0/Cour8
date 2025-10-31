import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# ---  Charger les données ---
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv'
df = pd.read_csv(url)

# ---  Nettoyage ---
df = df.dropna(subset=['Year', 'Automobile_Sales', 'Vehicle_Type', 'GDP', 'unemployment_rate', 'Advertising_Expenditure'])

# ---  Créer l'application ---
app = dash.Dash(__name__)

# ---  Mise en page ---
app.layout = html.Div([
    html.H1(
        "Statistiques annuelles des ventes d'automobiles",
        style={'textAlign': 'center', 'color': '#1f77b4', 'margin-bottom': '30px'}
    ),

    # Dropdown pour sélectionner l'année
    html.Div([
        html.Label("Sélectionnez l'année :"),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': str(i), 'value': i} for i in sorted(df['Year'].unique())],
            value=sorted(df['Year'].unique())[0],
            clearable=False
        )
    ], style={'width': '30%', 'padding': '10px'}),

    # Conteneur pour les graphiques (2x2)
    html.Div([
        html.Div([dcc.Graph(id='sales-graph')], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),
        html.Div([dcc.Graph(id='gdp-graph')], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),
        html.Div([dcc.Graph(id='unemployment-graph')], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),
        html.Div([dcc.Graph(id='ad-graph')], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),
    ])
])

# ---  Callbacks pour mettre à jour les graphiques ---
@app.callback(
    Output('sales-graph', 'figure'),
    Output('gdp-graph', 'figure'),
    Output('unemployment-graph', 'figure'),
    Output('ad-graph', 'figure'),
    Input('year-dropdown', 'value')
)
def update_annual_graphs(selected_year):
    # Filtrer les données selon l'année sélectionnée
    df_year = df[df['Year'] == selected_year]

    # Graphique 1 : ventes par type de véhicule
    fig_sales = px.bar(
        df_year.groupby('Vehicle_Type', as_index=False)['Automobile_Sales'].sum(),
        x='Vehicle_Type', y='Automobile_Sales',
        title=f"Ventes totales par type de véhicule - {selected_year}"
    )

    # Graphique 2 : PIB moyen
    fig_gdp = px.line(
        df.groupby('Year', as_index=False)['GDP'].mean(),
        x='Year', y='GDP',
        markers=True,
        title="Évolution du PIB moyen"
    )

    # Graphique 3 : taux de chômage
    fig_unemployment = px.line(
        df.groupby('Year', as_index=False)['unemployment_rate'].mean(),
        x='Year', y='unemployment_rate',
        markers=True,
        title="Évolution du taux de chômage moyen"
    )

    # Graphique 4 : dépenses publicitaires par type de véhicule
    fig_ad = px.pie(
        df_year.groupby('Vehicle_Type', as_index=False)['Advertising_Expenditure'].sum(),
        names='Vehicle_Type', values='Advertising_Expenditure',
        title=f"Dépenses publicitaires par type de véhicule - {selected_year}"
    )

    return fig_sales, fig_gdp, fig_unemployment, fig_ad

# ---  Lancer l'application ---
if __name__ == '__main__':
    app.run(debug=True)

