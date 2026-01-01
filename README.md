
# Enterprise Decision Intelligence System

An **Enterprise Decision Intelligence System** that transforms raw business data into **actionable recommendations** through analytics, scenario simulation, risk detection, and executive-level insights.

This project goes beyond dashboards by **interpreting KPIs**, evaluating **what-if scenarios**, and generating **decision recommendations with confidence scoring**.

---

## 🔍 Problem Statement

Enterprises often rely on static dashboards that show numbers but do not:
- Interpret business performance
- Recommend actions
- Evaluate scenario impact
- Highlight operational risks

This system bridges that gap by providing a **decision-oriented analytics platform**.

---

## 🚀 Key Features

### 1. Executive KPI Analytics
- Total Revenue
- Total Profit
- Best Performing Department
- KPI delta tracking (change awareness)

### 2. Decision Intelligence Engine
- Automated performance interpretation
- Actionable system recommendations
- Margin-based decision logic
- Decision confidence scoring

### 3. What-If Scenario Simulation
- User-driven revenue/cost simulations
- Profit impact comparison
- Scenario-based recommendations

### 4. Risk Detection
- Identifies loss-making departments
- Flags operational risk areas
- Integrates risk signals into recommendations

### 5. Interactive Analytics Dashboard
- Department-wise profit visualization
- Backend-driven insights
- Real-time refresh support

### 6. Data Export
- Export enterprise reports as CSV
- Suitable for audits, reporting, and presentations

---

## 🧠 System Architecture

```

Frontend (HTML/CSS/JS)
↓
FastAPI Backend
├── KPI Analytics
├── Decision Engine
├── Scenario Simulator
├── Risk Detection
└── Export Services
↓
Enterprise Data (CSV / Extendable to DB)

```

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Pandas
- Pydantic

### Frontend
- HTML5
- CSS3
- JavaScript (Vanilla)
- Chart.js

### Data
- Structured enterprise data (CSV)
- Easily extensible to PostgreSQL / MySQL

---

## 📂 Project Structure

```

enterprise_decision_intelligence/
│
├── app/
│   ├── api/              # API routes
│   ├── analytics/        # KPI & reporting logic
│   ├── data/             # Sample enterprise data
│   ├── ml/               # ML-ready decision models
│   └── dashboard/        # Frontend templates & static files
│
├── models/               # Saved ML models (optional)
├── requirements.txt
├── README.md
└── run.py

````

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/kuppireddybhageerathareddy1110/Enterprise-Decision-Intelligence-System.git
cd Enterprise-Decision-Intelligence-System
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv edi_env
edi_env\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
uvicorn app.main:app --reload
```

### 5️⃣ Open Dashboard

```
http://127.0.0.1:8000/
```

---

## 📡 API Endpoints

| Endpoint             | Method | Description               |
| -------------------- | ------ | ------------------------- |
| `/kpis`              | GET    | Fetch enterprise KPIs     |
| `/kpis/{department}` | GET    | Department-specific KPIs  |
| `/decision-insight`  | GET    | System recommendation     |
| `/scenario-compare`  | POST   | What-if scenario analysis |
| `/risk-flags`        | GET    | Risk detection            |
| `/calculate`         | POST   | Custom KPI calculation    |
| `/export`            | GET    | Export CSV report         |
| `/config`            | GET    | UI configuration          |

---

## 📊 Example Use Cases

* Executive performance review
* Department-level profitability analysis
* Financial risk identification
* Strategic planning using scenario modeling
* Decision support for management teams

---

## 📌 Domains Covered

* Decision Intelligence
* Business Intelligence (BI)
* Data Analytics & Data Science
* Enterprise Software Engineering
* Financial & Risk Analytics
* Applied Machine Learning (Decision Support)

---

## 🧩 Future Enhancements

* Database integration (PostgreSQL)
* ML-based recommendation scoring
* Role-based access (Analyst / Manager)
* PDF report generation
* React frontend

---

## 👤 Author

**Kuppireddy Bhageeratha Reddy**
B.Tech – Computer Science & Engineering
Focus Areas: Data Science, Decision Intelligence, Enterprise Systems

---

## 📄 License

This project is for educational and demonstration purposes.




