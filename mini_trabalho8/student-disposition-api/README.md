# Student Disposition Prediction API

Este README explica como configurar, treinar e rodar a API localmente.

## 1. Estrutura do Projeto

```
student-disposition-api/
├── app/
│   ├── main.py
│   └── schemas.py
├── models/
│   └── svm_disposition_model.pkl    # Será gerado após o treino
├── scripts/
│   └── train_model.py               # Script de treinamento
├── processed_dataset.csv            # Seu dataset pré-processado
├── requirements.txt                 # Dependências Python
├── Dockerfile                       # Para container Docker
└── README.md                        # Este arquivo
```

## 2. Pré-requisitos

- Python 3.8+ instalado
- pip (gerenciador de pacotes Python)
- (Opcional) Docker & Docker Compose
- (Opcional) Heroku CLI, se for deploy em Heroku

## 3. Instalar Dependências

No terminal, na raiz do projeto, execute:

```bash
pip install -r requirements.txt
```

## 4. Treinar o Modelo

O script de treinamento carrega seu dataset e salva o modelo otimizado em `models/`.

```bash
python scripts/train_model.py
```

Saída esperada:

```
Melhores parâmetros: {...}
Melhor acurácia CV: 0.97...
Modelo otimizado salvo em models/svm_disposition_model.pkl
```

## 5. Rodar a API Localmente

Após gerar o modelo:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- Acesse a documentação interativa: `http://localhost:8000/docs`  
- Endpoints principais:
  - `GET /` — Health check
  - `POST /predict` — Previsão de disposição

## 6. Testando o Endpoint `/predict`

No Swagger UI (`/docs`), clique em **POST /predict**, preencha o JSON de exemplo e clique em **Execute**. A resposta terá o formato:

```json
{
  "predicted_class": 0,
  "predicted_meaning": "Baixo estresse / Alta disposição",
  "classes": [
    { "class": 0, "meaning": "Baixo estresse / Alta disposição", "probability_percent": 98.7 },
    { "class": 1, "meaning": "Estresse médio / Disposição moderada", "probability_percent": 0.7 },
    { "class": 2, "meaning": "Alto estresse / Baixa disposição", "probability_percent": 0.5 }
  ]
}
```

## 7. (Opcional) Rodar com Docker

1. Build da imagem:
   ```bash
   docker build -t disposition-api .
   ```
2. Executar container:
   ```bash
   docker run -d -p 8000:8000 --name disposition-api disposition-api
   ```
3. Acesse `http://localhost:8000/docs`.
