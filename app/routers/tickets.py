from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, dependencies


router = APIRouter()

@router.post("/tickets")
def create_ticket(ticket: schemas.TicketCreate,
                  db: Session = Depends(dependencies.get_db),
                  user=Depends(dependencies.get_current_user)):

    new_ticket = models.Ticket(**ticket.dict(), created_by=user.id)
    db.add(new_ticket)
    db.commit()
    return new_ticket


@router.get("/tickets")
def list_tickets(db: Session = Depends(dependencies.get_db),
                 user=Depends(dependencies.get_current_user)):

    return db.query(models.Ticket).filter(models.Ticket.created_by == user.id).all()


@router.put("/tickets/{id}")
def update_ticket(id: int, data: schemas.TicketUpdate,
                  db: Session = Depends(dependencies.get_db),
                  user=Depends(dependencies.get_current_user)):

    ticket = db.query(models.Ticket).filter(models.Ticket.id == id).first()

    if ticket.created_by != user.id:
        return {"error": "Not allowed"}

    for key, value in data.dict(exclude_unset=True).items():
        setattr(ticket, key, value)

    db.commit()
    return ticket