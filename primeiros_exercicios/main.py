import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os

base_path = os.path.dirname(__file__)
file_name = os.path.join(base_path, '6_1_dados_elastic_net_regression.csv')

#fixar valores
fixed_alpha = 0.1
fixed_l1_ratio = 0.5

# carregar dados
try:
    print(f"Carregando dados do arquivo: {file_name}")
    data = pd.read_csv(file_name)
    print("Dados carregados com sucesso.")
    print("Primeiras 5 linhas dos dados:")
    print(data.head())

    # Separar features (X) e variável alvo (y)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    feature_names = X.columns.tolist()

    print(f"\nUsando {X.shape[1]} features: {feature_names}")
    print(f"Variável alvo: {data.columns[-1]}")

except FileNotFoundError:
    print(f"Erro: Arquivo '{file_name}' não encontrado.")
    exit()
except Exception as e:
    print(f"Erro ao carregar ou processar o arquivo: {e}")
    exit()

# Implementar e Treinar o Modelo (com parâmetros fixos)

print(f"\nCriando e treinando o modelo ElasticNet com alpha={fixed_alpha} e l1_ratio={fixed_l1_ratio}...")

modelo_elastic_net = ElasticNet(alpha=fixed_alpha, l1_ratio=fixed_l1_ratio, max_iter=10000, random_state=42)

# Treinar o modelo usando TODOS os dados
modelo_elastic_net.fit(X, y)
print("Modelo treinado.")

#avaliar o Modelo

# a) Obter coeficientes e intercepto
intercepto = modelo_elastic_net.intercept_
coeficientes = modelo_elastic_net.coef_

print("\n--- Avaliação Simplificada (sobre dados de treino) ---")
print(f"\nIntercepto (beta_0): {intercepto:.4f}")
print("Coeficientes (betas) por feature:")
for feature, coef in zip(feature_names, coeficientes):
    print(f"  {feature}: {coef:.4f}")

# Contar coeficientes zerados (efeito da regularização L1 dentro do ElasticNet)
zero_coeffs = np.sum(coeficientes == 0)
print(f"\nNúmero de coeficientes zerados pela regularização: {zero_coeffs} de {len(coeficientes)}")

# b) Fazer previsões (nos mesmos dados de treino)
print("\nRealizando previsões nos dados de treino...")
y_pred = modelo_elastic_net.predict(X)

# c) Calcular métricas (nos dados de treino - CUIDADO: pode superestimar o desempenho)
mse_treino = mean_squared_error(y, y_pred)
r2_treino = r2_score(y, y_pred)

print("\nMétricas de Desempenho (calculadas sobre os dados de treino):")
print(f"  Mean Squared Error (MSE): {mse_treino:.4f}")
print(f"  R-squared (R²): {r2_treino:.4f}")
print("  (Atenção: Métricas calculadas nos dados de treino podem indicar overfitting)")


# --- Plotagem Adaptada ---
# Como geralmente temos múltiplas features, plotar uma linha simples como nos exemplos
# (feature vs target) não é direto. Uma alternativa é plotar Real vs. Previsto.

plt.figure(figsize=(8, 6))
plt.scatter(y, y_pred, alpha=0.6, label='Previsões vs. Reais (Treino)')
# Adicionar linha ideal (y=x) para referência
min_val = min(y.min(), y_pred.min())
max_val = max(y.max(), y_pred.max())
plt.plot([min_val, max_val], [min_val, max_val], 'r--', label='Linha Ideal (y=x)')

plt.title(f'Elastic Net Regression (alpha={fixed_alpha}, l1_ratio={fixed_l1_ratio}) - Real vs. Previsto')
plt.xlabel('Valores Reais (y)')
plt.ylabel('Valores Previstos (ŷ)')
plt.legend()
plt.grid(True)
plt.show()

print("\n--- Exercício (Versão Simplificada) Concluído ---")