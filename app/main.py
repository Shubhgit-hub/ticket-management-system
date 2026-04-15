from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.database import Base, engine
from app.routers import auth, tickets, admin


# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


# include routers
app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(tickets.router, prefix="/api/v1")
app.include_router(admin.router, prefix="/api/v1")


# home route
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>Ticket Management System</h2>
    <p>API is running...</p>
    """