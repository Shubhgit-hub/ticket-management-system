from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, tickets, admin

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(tickets.router)
app.include_router(admin.router)
@app.get("/")
def home():
    return {"message": "API is running "}