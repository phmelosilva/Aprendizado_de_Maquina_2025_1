from pydantic import BaseModel

class DispositionRequest(BaseModel):
    Study_Hours_Per_Day: float
    Extracurricular_Hours_Per_Day: float
    Sleep_Hours_Per_Day: float
    Social_Hours_Per_Day: float
    Physical_Activity_Hours_Per_Day: float
