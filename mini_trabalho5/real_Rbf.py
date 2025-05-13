import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

# Exemplo de carregamento do dataset (substitua pelo seu arquivo)
df = pd.read_csv('./processed_dataset.csv') 
 # Substitua com o caminho correto
X = df.drop(columns=['Physical_Activity_Hours_Per_Day', 'Student_ID'])
y = df['Physical_Activity_Hours_Per_Day']

# Dividir dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo SVR com kernel RBF
model = SVR(kernel='rbf')
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
print("MSE:", mean_squared_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))

# Ordenar os valores reais para visualização
sorted_indices = np.argsort(y_test)
y_test_sorted = y_test[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]

# Plotar gráfico
plt.figure(figsize=(10, 5))
plt.plot(y_test_sorted, label='Valor Real', marker='o', linestyle='-', color='blue')
plt.plot(y_pred_sorted, label='Valor Previsto (RBF)', marker='x', linestyle='--', color='orange')
plt.title('Previsão da Disposição Diária com SVR (RBF)')
plt.xlabel('Amostras (ordenadas por valor real)')
plt.ylabel('Horas de Atividade Física por Dia')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()