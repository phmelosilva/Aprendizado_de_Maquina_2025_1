import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
'''
# 1. Gráfico de Dispersão: Duração do Sono vs Qualidade do Sono
plt.figure()
plt.scatter(df['Sleep Duration'], df['Quality of Sleep'])
plt.title('Duração do Sono vs Qualidade do Sono') 
plt.xlabel('Duração do Sono (horas)')           # Legenda eixo X
plt.ylabel('Qualidade do Sono (1-10)')          # Legenda eixo Y 
plt.show()
'''
# 2. Gráfico de Barras: Nível Médio de Atividade Física por Qualidade do Sono
avg_activity = df.groupby('Quality of Sleep')['Physical Activity Level'].mean().sort_index()

plt.figure()
plt.bar(avg_activity.index.astype(str), avg_activity.values)
plt.title('Nível Médio de Atividade Física por Qualidade do Sono')
plt.xlabel('Qualidade do Sono (1-10)')                            # Legenda eixo X 
plt.ylabel('Nível de Atividade Física (minutos/dia)')             # Legenda eixo Y 
plt.show()