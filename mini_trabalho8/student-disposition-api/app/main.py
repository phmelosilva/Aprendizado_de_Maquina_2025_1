import os
import joblib
from fastapi import FastAPI, HTTPException
from app.schemas import DispositionRequest
from typing import Dict, List, Any

# Mapeamento de classes para descrição
CLASS_MEANINGS = {
    0: "Baixo estresse / Alta disposição",
    1: "Estresse médio / Disposição moderada",
    2: "Alto estresse / Baixa disposição"
}

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'svm_disposition_model.pkl')

app = FastAPI(
    title="Disposition Prediction API",
    description="API para previsão de nível de disposição (Stress_Level_Encoded) a partir de hábitos de vida.",
    version="1.1.0"
)

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Não foi possível carregar o modelo: {e}")

@app.get("/")
async def health_check() -> Dict[str, str]:
    return {"status": "ok", "message": "API rodando"}

@app.post("/predict")
async def predict(payload: DispositionRequest) -> Dict[str, Any]:
    features = [[
        payload.Study_Hours_Per_Day,
        payload.Extracurricular_Hours_Per_Day,
        payload.Sleep_Hours_Per_Day,
        payload.Social_Hours_Per_Day,
        payload.Physical_Activity_Hours_Per_Day
    ]]
    try:
        probs = model.predict_proba(features)[0]
        predicted_class = int(probs.argmax())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Monta resposta detalhada por classe
    classes_info: List[Dict[str, Any]] = []
    for idx, p in enumerate(probs):
        classes_info.append({
            "class": idx,
            "meaning": CLASS_MEANINGS.get(idx, "Unknown"),
            "probability_percent": round(p * 100, 1)
        })

    return {
        "predicted_class": predicted_class,
        "predicted_meaning": CLASS_MEANINGS.get(predicted_class, "Unknown"),
        "classes": classes_info
    }
