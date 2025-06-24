# Student Disposition Prediction API

Este README explica como configurar, treinar, rodar a API localmente e garantir a qualidade em produção.

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

- Python 3.8+  
- pip (gerenciador de pacotes Python)  
- (Opcional) Docker & Docker Compose  
- (Opcional) Heroku CLI  

## 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

## 4. Treinar o Modelo

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

```bash
docker build -t disposition-api .
docker run -d -p 8000:8000 --name disposition-api disposition-api
```

Acesse `http://localhost:8000/docs`.

## 9. Monitoramento, Segurança e Estabilidade

Para garantir qualidade contínua:

**9.1 Monitoramento de Desempenho**  
- **Métricas em Tempo Real**: exponha latência, taxa de erro e throughput usando Prometheus + Grafana.  
- **Alertas**: configure notificações (e-mail, Slack) para latência acima de X ms ou aumento de 5% de erros em 10 minutos.  
- **Logs Estruturados**: use Python `logging` em JSON (inclusão de timestamp, payload, tempo de inferência).

**9.2 Testes de Segurança e Estabilidade**  
- **Teste de Carga**: utilize Locust ou JMeter para simular picos de concorrência (ex: 100 requisições/s).  
- **Teste de Penetração**: rode OWASP ZAP ou Burp Suite para identificar vulnerabilidades nas APIs.  
- **Validação de Input**: Pydantic valida esquemas, garantindo rejeição de JSON inválido (HTTP 422).  
- **Scan de Dependências**: use `pip-audit` ou `safety` diariamente para checar vulnerabilidades.

**9.3 Plano de Manutenção e Atualização**  
- **Re-treinamento Agendado**: crie pipeline (GitHub Actions, Airflow) para re-treinar modelo mensalmente.  
- **Versionamento de Modelo**: adote DVC ou MLflow para Version Control e rastreabilidade.  
- **Testes Automatizados**: inclua testes unitários e de integração no CI (GitHub Actions).  
- **Rollback Rápido**: mantenha última versão estável do modelo no bucket ou registry e prepare endpoint de fallback.

---

Com este projeto, você terá não apenas a API de predição, mas também o suporte necessário para monitorar, testar e manter seu modelo em produção de forma segura e estável.
