import dash
from dash import html, dcc

# --- 1️⃣ Création de l'application ---
app = dash.Dash(__name__)

# --- 2️⃣ Définition de la mise en page ---
app.layout = html.Div([
    # Titre principal
    html.H1(
        "Tableau de bord des statistiques de vente d'automobiles",
        style={
            'textAlign': 'center',    # Centrer le texte
            'color': '#1f77b4',       # Couleur du texte
            'font-family': 'Arial',
            'margin-bottom': '30px'
        }
    )
])

# --- 3️⃣ Lancer l'application ---
if __name__ == "__main__":
    app.run(debug=True)
