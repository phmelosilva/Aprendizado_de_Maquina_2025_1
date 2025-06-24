import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "API rodando" in data["message"]

def test_predict_endpoint():
    payload = {
        "Study_Hours_Per_Day": 5.0,
        "Extracurricular_Hours_Per_Day": 1.0,
        "Sleep_Hours_Per_Day": 7.0,
        "Social_Hours_Per_Day": 2.0,
        "Physical_Activity_Hours_Per_Day": 1.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    # Check keys in response
    assert "predicted_class" in data
    assert "predicted_meaning" in data
    assert "classes" in data
    # Check classes list format
    assert isinstance(data["classes"], list)
    for item in data["classes"]:
        assert "class" in item
        assert "meaning" in item
        assert "probability_percent" in item

if __name__ == "__main__":
    pytest.main()
