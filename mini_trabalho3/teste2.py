import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os CSVs
taco    = pd.read_csv('taco101.csv')    
sleep   = pd.read_csv('sleep101.csv')  

# 2. Merge por Person ID
df = taco.merge(
    sleep[['Person ID', 'Physical Activity Level', 'Quality of Sleep']],
    on='Person ID',
    how='inner'
)

# 3. Converter e limpar
df['Energy_Intake'] = pd.to_numeric(df['Energy_Intake'], errors='coerce')
df['Physical Activity Level'] = pd.to_numeric(df['Physical Activity Level'], errors='coerce')
df = df.dropna(subset=['Energy_Intake', 'Physical Activity Level'])

# 4. Scatter: Calorias vs. Atividade Física
plt.figure(figsize=(6,4))
plt.scatter(df['Energy_Intake'], df['Physical Activity Level'], alpha=0.6, s=10)
plt.xlabel('Ingestão Calórica (kcal/dia)')
plt.ylabel('Atividade Física (min/dia)')
plt.title('Calorias vs. Atividade Física')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('scatter_calorias_atividade.png')
plt.clf()

# 5. Bar plot por quintis (especificando observed)
df['Intake_Quintile'] = pd.qcut(df['Energy_Intake'], 5, labels=[1,2,3,4,5])
mean_act = df.groupby('Intake_Quintile', observed=False)['Physical Activity Level'].mean()

plt.figure(figsize=(6,4))
mean_act.plot(kind='bar', edgecolor='k')
plt.xlabel('Quintil de Ingestão Calórica (1–5)')
plt.ylabel('Média de Atividade Física (min/dia)')
plt.title('Atividade Média por Quintil de Calorias')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('bar_atividade_por_quintil.png')
plt.clf()