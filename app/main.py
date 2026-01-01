from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.api.routes import router

app = FastAPI(title="Enterprise Decision Intelligence System")

# APIs
app.include_router(router)

# Static files
app.mount("/static", StaticFiles(directory="app/dashboard/static"), name="static")

# Frontend route
@app.get("/", response_class=HTMLResponse)
def dashboard():
    with open("app/dashboard/templates/index.html", encoding="utf-8") as f:
        return f.read()
