import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Carregar o dataset
data = pd.read_csv('student_lifestyle_dataset.csv')

# 1. Tratamento de valores ausentes
# Verificar valores ausentes
print("TRATAMENTO DE VALORES AUSENTES")
print("Valores ausentes antes do tratamento:")
print(data.isnull().sum())

# Preencher valores ausentes com a mediana para colunas numéricas
numeric_columns = data.select_dtypes(include=[np.number]).columns
for col in numeric_columns:
    data[col] = data[col].fillna(data[col].median())

# Preencher valores ausentes com a moda para a coluna categórica 'Stress_Level'
data['Stress_Level'] = data['Stress_Level'].fillna(data['Stress_Level'].mode()[0])

# Verificar valores ausentes após o tratamento
print("\nValores ausentes após o tratamento:")
print(data.isnull().sum())
print('--'*50)
print("TRATAMENTO DE OUTLIERS")
# 2. Detecção e tratamento de outliers usando IQR
def treat_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    print(f"\nResumo estatístico da coluna '{column}':")
    print(f"Q1: {Q1}")
    print(f"Q3: {Q3}")
    print(f"IQR: {IQR}")
    print(f"Limite inferior: {lower_bound}")
    print(f"Limite superior: {upper_bound}")
    outlier_condition = (df[column] < lower_bound) | (df[column] > upper_bound)
    outliers = outlier_condition.sum()
    print(f"Outliers encontrados na coluna '{column}': {outliers}")
    if outliers > 0:
        print(f"\nDetalhes dos outliers na coluna '{column}':")
        print(df[outlier_condition][[column]])
        df = df[~outlier_condition]
        print(f"{outliers} registros removidos da coluna '{column}' por serem outliers.")
    else:
        print(f"Nenhum outlier foi encontrado na coluna '{column}'. Nenhuma linha foi removida.")
    return df

# Aplicar tratamento de outliers para colunas numéricas (exceto Student_ID)
for col in numeric_columns:
    if col != 'Student_ID':
        data = treat_outliers(data, col)

print('--'*50)
print("TRATAMENTO DE VARIÁVEIS CATEGÓRICAS")
# 3. Codificação da variável categórica 'Stress_Level'
label_encoder = LabelEncoder()
label_encoder.fit(data['Stress_Level'])

print("\nMapeamento de valores categóricos para numéricos (Stress_Level):")
for idx, class_name in enumerate(label_encoder.classes_):
    print(f"{class_name} → {idx}")

data['Stress_Level_Encoded'] = label_encoder.transform(data['Stress_Level'])

# 4. Normalização/Padronização das características numéricas
# Selecionar colunas para padronização (excluindo Student_ID e Stress_Level_Encoded)
features_to_scale = ['Study_Hours_Per_Day', 'Extracurricular_Hours_Per_Day', 
                    'Sleep_Hours_Per_Day', 'Social_Hours_Per_Day', 
                    'Physical_Activity_Hours_Per_Day', 'GPA']

scaler = StandardScaler()
data[features_to_scale] = scaler.fit_transform(data[features_to_scale])

# 5. Remover a coluna original 'Stress_Level' após codificação
data = data.drop('Stress_Level', axis=1)

# 6. Salvar o dataset processado
data.to_csv('processed_dataset.csv', index=False)
