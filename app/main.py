from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, tickets, admin

Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url=None, redoc_url=None)


app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(tickets.router, prefix="/api/v1/tickets")
app.include_router(admin.router, prefix="/api/v1/admin")
@app.get("/")
def home():
    return {"message": "API is running "}
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Ticket Management System</h1>
    <p>Backend is running successfully 🚀</p>
    """