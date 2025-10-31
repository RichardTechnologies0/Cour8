import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# --- Charger les données ---
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv'
df = pd.read_csv(url)

# --- Créer l'application ---
app = dash.Dash(__name__)

# --- Mise en page ---
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

    # Dropdown pour sélectionner l'année (désactivé par défaut)
    html.Div([
        html.Label("Saisir l'année :"),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': str(i), 'value': i} for i in range(2000, 2024)],
            value=None,
            disabled=True
        )
    ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px'}),

    # Conteneur pour afficher les informations d'entrée
    html.Div(
        id='input-container',
        className='input-container',
        children="Informations sur le type de statistique sélectionné apparaîtront ici.",
        style={'marginTop': '20px', 'padding': '15px', 'border': '1px solid #ccc'}
    ),

    # Conteneur pour afficher les graphiques
    html.Div(
        id='output-container',
        className='output-container',
        children="Les graphiques apparaîtront ici.",
        style={'marginTop': '20px', 'padding': '15px', 'border': '1px solid #ccc'}
    )
])

@app.callback(
    Output('input-container', 'children'),
    Output('year-dropdown', 'disabled'),
    Input('stats-dropdown', 'value')
)
def update_input_container(selected_stat):

    enable_year = selected_stat in ['total_sales', 'ad_exp']

    text = f"Statistique sélectionnée : {selected_stat.replace('_', ' ').title()}."
    if enable_year:
        text += " Vous pouvez maintenant sélectionner l'année."
    else:
        text += " La sélection d'année est désactivée pour cette statistique."

    return text, not enable_year



@app.callback(
    Output('output-container', 'children'),
    Input('stats-dropdown', 'value'),
    Input('year-dropdown', 'value')
)
def update_graph(selected_stat, selected_year):

    filtered_df = df.copy()
    if selected_year is not None:
        filtered_df = filtered_df[filtered_df['Year'] == selected_year]

    if selected_stat == 'total_sales':
        fig_df = filtered_df.groupby('Vehicle_Type', as_index=False)['Automobile_Sales'].sum()
        fig = px.bar(fig_df, x='Vehicle_Type', y='Automobile_Sales', title="Ventes totales par type de véhicule")
    elif selected_stat == 'ad_exp':
        fig_df = filtered_df.groupby('Vehicle_Type', as_index=False)['Advertising_Expenditure'].sum()
        fig = px.bar(fig_df, x='Vehicle_Type', y='Advertising_Expenditure',
                     title="Dépenses publicitaires par type de véhicule")
    elif selected_stat == 'gdp':
        fig_df = filtered_df.groupby('Year', as_index=False)['GDP'].mean()
        fig = px.line(fig_df, x='Year', y='GDP', title="Évolution du PIB moyen")
    elif selected_stat == 'unemployment':
        fig_df = filtered_df.groupby('Year', as_index=False)['unemployment_rate'].mean()
        fig = px.line(fig_df, x='Year', y='unemployment_rate', title="Évolution du taux de chômage moyen")
    else:
        return "Sélectionnez une statistique valide."

    return dcc.Graph(figure=fig)


# --- Lancer l'application ---
if __name__ == '__main__':
    app.run(debug=True)
