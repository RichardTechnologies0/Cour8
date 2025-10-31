import pandas as pd
import matplotlib.pyplot as plt

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv'
df = pd.read_csv(url)

ventes_annuelles = df.groupby('Year')['Automobile_Sales'].sum().reset_index()

plt.figure(figsize=(10,6))
plt.plot(ventes_annuelles['Year'], ventes_annuelles['Automobile_Sales'], marker='o', color='blue')


plt.title("Évolution des ventes d'automobiles par année", fontsize=14)
plt.xlabel("Année")
plt.ylabel("Ventes d'automobiles")
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(ventes_annuelles['Year'], rotation=45)
plt.tight_layout()


plt.show()
