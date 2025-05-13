import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 

# Carrega os dados do arquivo CSV
caminho_csv = './processed_dataset.csv'
dados = pd.read_csv(caminho_csv)

# Define a variável independente (X) e a variável alvo (y)
X = dados[['Study_Hours_Per_Day']].values
y = dados['Physical_Activity_Hours_Per_Day'].values

# Divide os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treina o modelo SVR com kernel RBF
modelo_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1)
modelo_rbf.fit(X_train, y_train)

# Faz previsões com o modelo
y_pred = modelo_rbf.predict(X_test)

# Avaliação do modelo (opcional, mas útil)
rmse = sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

# Gráfico de comparação entre valores reais e previstos
plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, color='purple')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='black', linestyle='--', label='Ideal')
plt.title('Comparação entre Valores Reais e Previstos - SVR RBF')
plt.xlabel('Valor Real (Horas de Atividade Física)')
plt.ylabel('Valor Previsto')
plt.legend()
plt.grid(True)
plt.show()

# Exibe métricas de avaliação
print(f'RMSE: {rmse:.4f}')
print(f'R²: {r2:.4f}')
