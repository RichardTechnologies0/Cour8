import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv'
df = pd.read_csv(url)

df_recession = df[df['Recession'] == 1].dropna(subset=['unemployment_rate', 'Automobile_Sales', 'Vehicle_Type'])

plt.figure(figsize=(10, 6))
sns.lineplot(
    data=df_recession,
    x='unemployment_rate',
    y='Automobile_Sales',
    hue='Vehicle_Type',
    marker='o',
    palette='Set2'
)

plt.title("Impact du taux de chômage sur les ventes d'automobiles par type de véhicule\n(période de récession)", fontsize=13)
plt.xlabel("Taux de chômage (%)")
plt.ylabel("Ventes d'automobiles")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title="Type de véhicule")
plt.tight_layout()
plt.show()
