import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


df = pd.read_csv('Exercicio-4.1/dados_bicicletas.csv')
 

X = df['Temperatura_Media'].values.reshape(-1, 1)  
y = df['Bicicletas_Alugadas'].values  


modelo = LinearRegression()
modelo.fit(X, y)


inclinacao = modelo.coef_[0]
intercepto = modelo.intercept_

temperaturas_teste = np.array([15, 20, 25, 30]).reshape(-1, 1)
previsoes = modelo.predict(temperaturas_teste)

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', alpha=0.5, label='Dados reais')
plt.plot(X, modelo.predict(X), color='red', label='Linha de regressão')
plt.xlabel('Temperatura Média (°C)')
plt.ylabel('Bicicletas Alugadas')
plt.title('Regressão Linear: Temperatura vs Bicicletas Alugadas')
plt.legend()
plt.grid(True)

print(f"Coeficiente de inclinação (slope): {inclinacao:.2f}")
print(f"Intercepto: {intercepto:.2f}")
print("\nPrevisões para temperaturas específicas:")
for temp, pred in zip(temperaturas_teste, previsoes):
    print(f"Temperatura {temp[0]}°C: {pred:.2f} bicicletas alugadas")

plt.show()