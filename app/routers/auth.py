from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, auth, dependencies
router = APIRouter()

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    hashed = auth.hash_password(user.password)
    db_user = models.User(username=user.username, email=user.email, password=hashed)
    db.add(db_user)
    db.commit()
    return {"msg": "User created"}

@router.post("/login")
def login(data: schemas.Login, db: Session = Depends(dependencies.get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()

    if not user or not auth.verify_password(data.password, user.password):
        return {"error": "Invalid credentials"}

    token = auth.create_token({"id": user.id})
    return {"token": token}