from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from app.data.loader import load_data
from app.analytics.kpi import calculate_kpis
from app.analytics.reports import department_summary
from app.ml.model import load_model, predict_growth
import pandas as pd
import os
import io

router = APIRouter()

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

DATA_PATH = os.path.join(BASE_DIR, "app", "data", "sample_data.csv")


@router.get("/kpis")
def get_kpis():
    df = load_data(DATA_PATH)
    return calculate_kpis(df)


@router.get("/kpis/{department}")
def get_kpis_by_department(department: str):
    df = load_data(DATA_PATH)
    if department.lower() != "all":
        df = df[df["department"].str.lower() == department.lower()]
    return calculate_kpis(df)


@router.get("/report")
def get_report():
    df = load_data(DATA_PATH)
    return department_summary(df)


@router.get("/config")
def get_config():
    return {
        "currency_symbol": "₹",
        "refresh_interval": 10
    }


class CalcInput(BaseModel):
    revenue: float
    cost: float
    employees: int


@router.post("/calculate")
def calculate(input: CalcInput):
    if input.employees <= 0:
        raise HTTPException(400, "Employees must be greater than zero")

    profit = input.revenue - input.cost
    rev_per_emp = input.revenue / input.employees

    return {
        "profit": round(profit, 2),
        "revenue_per_employee": round(rev_per_emp, 2)
    }


@router.get("/export")
def export_csv():
    df = load_data(DATA_PATH)

    stream = io.StringIO()
    df.to_csv(stream, index=False)
    stream.seek(0)

    return StreamingResponse(
        stream,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=decision_report.csv"}
    )
@router.get("/decision-insight")
def decision_insight():
    df = load_data(DATA_PATH)
    kpis = calculate_kpis(df)

    revenue = kpis["total_revenue"]
    profit = kpis["total_profit"]

    if revenue == 0:
        return {
            "message": "Insufficient data to evaluate performance.",
            "level": "warning",
            "margin": 0
        }

    margin = profit / revenue

    if margin < 0:
        return {
            "message": "🚨 Organization is running at a loss. Immediate intervention required.",
            "level": "critical",
            "margin": round(margin * 100, 2)
        }

    if margin < 0.2:
        return {
            "message": "⚠️ Profit margins are low. Cost optimization is recommended.",
            "level": "warning",
            "margin": round(margin * 100, 2)
        }

    return {
        "message": "✅ Financial performance is healthy. Maintain current strategy.",
        "level": "good",
        "margin": round(margin * 100, 2)
    }

class ScenarioInput(BaseModel):
    current_revenue: float
    current_cost: float
    scenario_revenue: float
    scenario_cost: float

@router.post("/scenario-compare")
def scenario_compare(input: ScenarioInput):
    current_profit = input.current_revenue - input.current_cost
    scenario_profit = input.scenario_revenue - input.scenario_cost
    delta = scenario_profit - current_profit

    if delta > 0:
        rec = "Scenario improves profitability. Recommended for consideration."
    else:
        rec = "Scenario does not improve profitability. Re-evaluation advised."

    return {
        "current_profit": round(current_profit, 2),
        "scenario_profit": round(scenario_profit, 2),
        "difference": round(delta, 2),
        "recommendation": rec
    }
@router.get("/risk-flags")
def risk_flags():
    df = load_data(DATA_PATH)
    df["profit"] = df["revenue"] - df["cost"]

    risky = df[df["profit"] < 0]["department"].tolist()

    return {
        "risk_departments": risky,
        "count": len(risky)
    }
