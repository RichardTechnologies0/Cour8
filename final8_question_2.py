import pandas as pd
import matplotlib.pyplot as plt


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv'
df = pd.read_csv(url)


df = df[['Year', 'Automobile_Sales', 'Vehicle_Type', 'Recession']]


ventes_type = df.groupby(['Year', 'Vehicle_Type'], as_index=False)['Automobile_Sales'].sum()


plt.figure(figsize=(12,6))
for veh_type in ventes_type['Vehicle_Type'].unique():
    subset = ventes_type[ventes_type['Vehicle_Type'] == veh_type]
    plt.plot(subset['Year'], subset['Automobile_Sales'], marker='o', label=veh_type)


plt.title("Évolution des ventes par type de véhicule", fontsize=14)
plt.xlabel("Année")
plt.ylabel("Ventes d'automobiles")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title="Type de véhicule")
plt.xticks(ventes_type['Year'].unique(), rotation=45)
plt.tight_layout()
plt.show()
