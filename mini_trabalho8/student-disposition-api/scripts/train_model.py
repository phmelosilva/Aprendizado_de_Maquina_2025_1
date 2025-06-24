import os
import pandas as pd
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'processed_dataset.csv')
MODEL_OUT = os.path.join(os.path.dirname(__file__), '..', 'models', 'svm_disposition_model.pkl')
os.makedirs(os.path.dirname(MODEL_OUT), exist_ok=True)

df = pd.read_csv(DATA_PATH)
X = df[['Study_Hours_Per_Day','Extracurricular_Hours_Per_Day',
        'Sleep_Hours_Per_Day','Social_Hours_Per_Day',
        'Physical_Activity_Hours_Per_Day']]
y = df['Stress_Level_Encoded']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(probability=True))
])
param_grid = {
    'svm__kernel': ['linear','rbf','poly'],
    'svm__C': [0.1,1,10,100],
    'svm__gamma': ['scale','auto'],
    'svm__degree': [2,3,4]
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
grid = GridSearchCV(pipeline, param_grid,
                    cv=cv, scoring='accuracy',
                    n_jobs=-1, verbose=1)
grid.fit(X_train, y_train)

print("Melhores parâmetros:", grid.best_params_)
print("Melhor acurácia CV:", grid.best_score_)

joblib.dump(grid.best_estimator_, MODEL_OUT)
print(f"Modelo otimizado salvo em {MODEL_OUT}")
