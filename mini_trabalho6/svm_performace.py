import pandas as pd                              # Importa pandas para manipulação de DataFrames
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split  # Importa funções para divisão de dados e busca de hiperparâmetros
from sklearn.svm import SVC                      # Importa o classificador SVM
from sklearn.preprocessing import StandardScaler  # Importa o scaler para normalizar as features
from sklearn.pipeline import Pipeline             # Importa Pipeline para encadear pré-processamento e modelo
from sklearn import metrics                      # Importa métricas para avaliação do modelo
from sklearn.metrics import ConfusionMatrixDisplay  # Importa utilitário para plotar matriz de confusão
import matplotlib.pyplot as plt                   # Importa matplotlib para plotar gráficos

# 1. Carregar o dataset / Load the dataset
df = pd.read_csv('processed_dataset.csv')         # Lê o arquivo CSV em um DataFrame

# 2. Definir X (features de lifestyle) e y (Stress_Level_Encoded)
X = df[[                                          # Seleciona colunas de estilo de vida como preditoras
    'Study_Hours_Per_Day',                        #   Horas de estudo por dia
    'Extracurricular_Hours_Per_Day',              #   Horas de atividades extracurriculares por dia
    'Sleep_Hours_Per_Day',                        #   Horas de sono por dia
    'Social_Hours_Per_Day',                       #   Horas de interação social por dia
    'Physical_Activity_Hours_Per_Day'             #   Horas de atividade física por dia
]]
y = df['Stress_Level_Encoded']                    # Define o rótulo: nível de estresse/disposição codificado numericamente

# 3. Divisão treino/teste / Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,                                         #   Entradas X e rótulos y
    test_size=0.2,                                #   20% dos dados para teste
    stratify=y,                                   #   Mantém proporção de classes em treino e teste
    random_state=42                               #   Semente para reprodutibilidade
)

# 4. Pipeline: normalização + SVM / Pipeline: scaling + SVM
pipeline = Pipeline([
    ('scaler', StandardScaler()),                 #   Aplica StandardScaler às features
    ('svm', SVC(probability=True))                 #   Treina SVC com probabilidade habilitada
])

# 5. Grade de hiperparâmetros / Hyperparameter grid
param_grid = {
    'svm__kernel': ['linear', 'rbf', 'poly'],     #   Tipos de kernel a testar
    'svm__C':      [0.1, 1, 10, 100],              #   Valores de regularização C
    'svm__gamma':  ['scale', 'auto'],              #   Estratégias de gamma para kernels não lineares
    'svm__degree': [2, 3, 4]                       #   Grau do polinômio (apenas para kernel='poly')
}

# 6. GridSearch + validação cruzada estratificada / GridSearch + stratified CV
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)  # Define 5 dobras estratificadas
grid = GridSearchCV(
    estimator=pipeline,                            #   Pipeline com scaler + SVM
    param_grid=param_grid,                        #   Grade de hiperparâmetros definida acima
    cv=cv,                                        #   Validação cruzada estratificada
    scoring='accuracy',                           #   Métrica de otimização: acurácia
    n_jobs=-1,                                    #   Usa todos os núcleos de CPU disponíveis
    verbose=1                                     #   Exibe progresso
)
grid.fit(X_train, y_train)                        # Executa a busca e treina o melhor modelo nos dados de treino

# 7. Resultados da busca de hiperparâmetros / Hyperparameter search results
print("===== RESULTADOS DA BUSCA DE HIPERPARÂMETROS =====")
print(f"Melhores parâmetros encontrados: {grid.best_params_}  (Best parameters found)")
print(f"Melhor acurácia média na validação cruzada: {grid.best_score_:.4f}  (Best mean CV accuracy)")

# 8. Avaliação de performance no conjunto de teste / Test set evaluation
y_pred = grid.predict(X_test)                     # Gera previsões no conjunto de teste
performance = {
    'Accuracy' : metrics.accuracy_score(y_test, y_pred),                    # Calcula acurácia
    'Precision': metrics.precision_score(y_test, y_pred, average='weighted'),  # Calcula precision ponderado
    'Recall'   : metrics.recall_score(y_test, y_pred, average='weighted'),     # Calcula recall ponderado
    'F1-Score' : metrics.f1_score(y_test, y_pred, average='weighted')          # Calcula F1-score ponderado
}

print("\n===== AVALIAÇÃO NO CONJUNTO DE TESTE =====")
print(f"Acurácia: {performance['Accuracy']:.4f}  (Accuracy)")
print(f"Precisão (média ponderada): {performance['Precision']:.4f}  (Precision, weighted)")
print(f"Revocação (Recall): {performance['Recall']:.4f}  (Recall)")
print(f"F1-Score: {performance['F1-Score']:.4f}  (F1-Score)")

# 9. Matriz de confusão / Confusion matrix
disp = ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred,                              #   Dados reais e previstos
    display_labels=grid.classes_,                #   Rótulos das classes
    cmap=plt.cm.Blues,                           #   Paleta de cores azul
    normalize=None                               #   Exibe contagens brutas
)
disp.ax_.set_title("Matriz de Confusão  (Confusion Matrix)")  # Título bilíngue
plt.show()                                        # Exibe o gráfico
