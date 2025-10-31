import pandas as pd
import matplotlib.pyplot as plt

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv'
df = pd.read_csv(url)

df_recession = df[df['Recession'] == 1].dropna(subset=['Advertising_Expenditure', 'Vehicle_Type'])

pub_par_type = df_recession.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    pub_par_type,
    labels=pub_par_type.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.Set3.colors,
    explode=[0.05]*len(pub_par_type),
    shadow=True
)

plt.title("Répartition des dépenses publicitaires par type de véhicule\npendant la période de récession", fontsize=13)
plt.tight_layout()
plt.show()
