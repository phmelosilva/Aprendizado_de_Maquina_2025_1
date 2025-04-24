import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os CSVs
taco = pd.read_csv('taco101.csv')
sleep = pd.read_csv('sleep101.csv') # sono, atividade, idade, gênero, (e BMI Category)

# 2. Imputar altura média e IMC médio estimados
#    (substitua pelos valores que tiver disponível, por faixa etária se possível)
altura_media = {'Male': 1.73, 'Female': 1.60}
imc_medio    = {
    'Normal': 22.5,
    'Normal Weight': 22.5,
    'Overweight': 27.5,
    'Obese': 32.5
}

# 3. Calcular peso estimado a partir de IMC e altura
sleep['Altura_m']   = sleep['Gender'].map(altura_media)
sleep['IMC_est']    = sleep['BMI Category'].map(imc_medio)
sleep['Peso_kg']    = sleep['IMC_est'] * sleep['Altura_m']**2

# 4. MB (Metabolismo Basal) pela fórmula de Mifflin–St Jeor
def calc_mb(row):
    h_cm = row['Altura_m'] * 100
    if row['Gender'] == 'Male':
        return 10*row['Peso_kg'] + 6.25*h_cm - 5*row['Age'] + 5
    else:
        return 10*row['Peso_kg'] + 6.25*h_cm - 5*row['Age'] - 161

sleep['Metabolismo_Basal'] = sleep.apply(calc_mb, axis=1)

# 5. Fator de atividade e GET (Gasto Energético Total)
def fator_atividade(mins):
    """
    Fator de Atividade Física:
      • < 30 min/dia → sedentário → 1.2
      • 30–59 min/dia → leve       → 1.375
      • 60–149 min/dia → moderado  → 1.55
      • ≥ 150 min/dia → alto       → 1.725
    """
    if mins < 30:
        return 1.2      # sedentário
    elif mins < 60:
        return 1.375    # leve
    elif mins < 150:
        return 1.55     # moderado
    else:
        return 1.725    # alto

sleep['Fator_Atividade'] = sleep['Physical Activity Level'].astype(float).apply(fator_atividade)
sleep['Gasto_Energetico_Total'] = sleep['Metabolismo_Basal'] * sleep['Fator_Atividade']

# 6. Juntar TDEE/GET (Gasto Energético Total) de volta ao consumo
#    e converter Energy_Intake para numérico
taco['Energy_Intake'] = pd.to_numeric(taco['Energy_Intake'], errors='coerce')
df = (
    taco
    .merge(
        sleep[['Person ID', 'Gasto_Energetico_Total']],
        on='Person ID',
        how='inner'
    )
    .dropna(subset=['Energy_Intake'])
)

# 7. Agregar ingestão total por pessoa e calcular balanço
resumo = (
    df
    .groupby('Person ID')
    .agg({
        'Energy_Intake': 'sum',
        'Gasto_Energetico_Total': 'first'
    })
    .rename(columns={
        'Energy_Intake': 'Ingestao_Total_kcal',
        'Gasto_Energetico_Total': 'GET_kcal'
    })
    .reset_index()
)
resumo['Balanco_kcal'] = resumo['Ingestao_Total_kcal'] - resumo['GET_kcal']

# 8. Gráfico: Consumo vs GET
plt.figure(figsize=(6,4))
plt.scatter(resumo['GET_kcal'], resumo['Ingestao_Total_kcal'], alpha=0.6, s=20)
plt.plot(
    [resumo['GET_kcal'].min(), resumo['GET_kcal'].max()],
    [resumo['GET_kcal'].min(), resumo['GET_kcal'].max()],
    'k--', lw=1
)
plt.xlabel('GET estimado (kcal/dia)')
plt.ylabel('Ingestão Total (kcal/dia)')
plt.title('Consumo Calórico vs. GET')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('consumo_vs_get.png')
plt.clf()

# 9. Histograma de Balanço Energético
plt.figure(figsize=(6,4))
plt.hist(resumo['Balanco_kcal'], bins=20, edgecolor='k')
plt.axvline(0, color='r', linestyle='--')
plt.xlabel('Balanço Energético (kcal/dia)')
plt.title('Distribuição do Balanço Energético')
plt.tight_layout()
plt.savefig('hist_balanco.png')
plt.clf()