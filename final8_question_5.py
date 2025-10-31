import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv'

df = pd.read_csv(url)

df = df.dropna(subset=['Seasonality_Weight', 'Automobile_Sales', 'Advertising_Expenditure', 'Vehicle_Type'])


plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='Seasonality_Weight',
    y='Automobile_Sales',
    size='Advertising_Expenditure',
    hue='Vehicle_Type',
    sizes=(50, 600),
    alpha=0.6,                       
    palette='Set2'
)

plt.title("Impact de la saisonnalité sur les ventes d’automobiles", fontsize=14)
plt.xlabel("Indice de saisonnalité")
plt.ylabel("Ventes d’automobiles")
plt.legend(title="Type de véhicule", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()