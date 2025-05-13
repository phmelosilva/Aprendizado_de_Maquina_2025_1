import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Carrega os dados
caminho_csv = './processed_dataset.csv'
dados = pd.read_csv(caminho_csv)

# Define a variável independente (X) e a variável alvo (y)
X = dados[['Stress_Level_Encoded']].values
y = dados['Physical_Activity_Hours_Per_Day'].values

# Cria e treina o modelo Ridge
modelo_ridge = Ridge(alpha=1.0)
modelo_ridge.fit(X, y)

# Obtém intercepto e coeficiente
intercepto = modelo_ridge.intercept_
coeficiente = modelo_ridge.coef_[0]

# Faz previsões
y_pred = modelo_ridge.predict(X)

# Plota os dados e a linha de ajuste
plt.scatter(X, y, color='blue', label='Dados Reais')
plt.plot(X, y_pred, color='green', label='Ridge - Previsão')
plt.title('Atividade Física vs. Nível de Estresse')
plt.xlabel('Nível de Estresse (Codificado)')
plt.ylabel('Horas de Atividade Física por Dia')
plt.legend()
plt.show()

# Exibe os parâmetros do modelo
print(f'Intercepto: {intercepto}')
print(f'Coeficiente para Stress_Level_Encoded: {coeficiente}')
