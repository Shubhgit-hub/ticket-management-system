from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, dependencies

router = APIRouter()

@router.get("/admin/tickets")
def all_tickets(db: Session = Depends(dependencies.get_db),
                user=Depends(dependencies.get_current_user)):

    if user.role != "admin":
        return {"error": "Admin only"}

    return db.query(models.Ticket).all()


@router.get("/admin/stats")
def stats(db: Session = Depends(dependencies.get_db),
          user=Depends(dependencies.get_current_user)):

    if user.role != "admin":
        return {"error": "Admin only"}

    total = db.query(models.Ticket).count()
    open_tickets = db.query(models.Ticket).filter(models.Ticket.status == "open").count()

    return {
        "total": total,
        "open": open_tickets
    }