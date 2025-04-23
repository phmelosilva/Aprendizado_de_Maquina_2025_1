import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet
import matplotlib.pyplot as plt

# Carregar os dados
caminho_csv = '6.1 - dados_elastic_net_regression.csv state=42)
modelo_elastic.fit(X, y)

# Coeficientes do modelo
intercepto = modelo_elastic.intercept_
coeficientes = modelo_elastic.coef_

# Previsões
y_pred = modelo_elastic.predict(X)

# Exibir os coeficientes
print(f'Intercepto: {intercepto:.4f}')
for i, coef in enumerate(coeficientes, 1):
    print(f'Coeficiente da Feature_{i}: {coef:.4f}')

# Visualização (usaremos apenas uma feature para visualização simples)
plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], y, color='blue', label='Dados reais (Feature_1)')
plt.scatter(X[:, 0], y_pred, color='red', label='Previsões', alpha=0.6)
plt.title('Elastic Net Regression (visualização usando Feature_1)')
plt.xlabel('Feature_1')
plt.ylabel('Target')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
