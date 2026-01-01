from pydantic import BaseModel

class PredictionInput(BaseModel):
    revenue: float
    cost: float
    employees: int
