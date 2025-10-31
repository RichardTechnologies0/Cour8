import pandas as pd
import matplotlib.pyplot as plt

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv'
df = pd.read_csv(url)


df_recession = df[df['Recession'] == 1]


df_recession = df_recession.dropna(subset=['Price', 'Automobile_Sales'])

plt.figure(figsize=(8, 6))
plt.scatter(
    df_recession['Price'],
    df_recession['Automobile_Sales'],
    color='tomato',
    alpha=0.6,
    edgecolor='k'
)

plt.title("Corrélation entre le prix moyen des véhicules et le volume des ventes\n(période de récession)", fontsize=13)
plt.xlabel("Prix moyen des véhicules")
plt.ylabel("Volume des ventes d'automobiles")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
