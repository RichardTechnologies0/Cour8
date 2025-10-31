import pandas as pd
import matplotlib.pyplot as plt

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv'
df = pd.read_csv(url)

df = df.dropna(subset=['Advertising_Expenditure', 'Recession'])


pub_totales = df.groupby('Recession')['Advertising_Expenditure'].sum()

labels = ['Hors récession', 'Récession']  # 0 = hors récession, 1 = récession


plt.figure(figsize=(6, 6))
plt.pie(
    pub_totales,
    labels=labels,
    autopct='%1.1f%%',        # pourcentage sur le graphique
    startangle=90,            # rotation du diagramme
    colors=['#66b3ff', '#ff9999'],
    explode=(0.05, 0.05),     # légère séparation pour les deux parts
    shadow=True
)

plt.title("Répartition des dépenses publicitaires de XYZAutomotives\nselon la période économique", fontsize=13)
plt.tight_layout()
plt.show()
