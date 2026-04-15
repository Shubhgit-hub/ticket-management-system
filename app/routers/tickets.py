from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, dependencies

router = APIRouter()


# create ticket
@router.post("/tickets")
def create_ticket(
    ticket: schemas.TicketCreate,
    db: Session = Depends(dependencies.get_db),
    user=Depends(dependencies.get_current_user)
):
    new_ticket = models.Ticket(**ticket.dict(), created_by=user.id)
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket


# list tickets (with optional filters)
@router.get("/tickets")
def list_tickets(
    status: str = None,
    priority: str = None,
    db: Session = Depends(dependencies.get_db),
    user=Depends(dependencies.get_current_user)
):
    query = db.query(models.Ticket).filter(models.Ticket.created_by == user.id)

    if status:
        query = query.filter(models.Ticket.status == status)

    if priority:
        query = query.filter(models.Ticket.priority == priority)

    return query.all()


# get ticket by id
@router.get("/tickets/{id}")
def get_ticket(
    id: int,
    db: Session = Depends(dependencies.get_db),
    user=Depends(dependencies.get_current_user)
):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == id).first()

    if not ticket or ticket.created_by != user.id:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return ticket


# update ticket
@router.put("/tickets/{id}")
def update_ticket(
    id: int,
    data: schemas.TicketUpdate,
    db: Session = Depends(dependencies.get_db),
    user=Depends(dependencies.get_current_user)
):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == id).first()

    if not ticket or ticket.created_by != user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(ticket, key, value)

    db.commit()
    db.refresh(ticket)
    return ticket


# update ticket status
@router.patch("/tickets/{id}/status")
def update_status(
    id: int,
    status: str,
    db: Session = Depends(dependencies.get_db),
    user=Depends(dependencies.get_current_user)
):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == id).first()

    if not ticket or ticket.created_by != user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    ticket.status = status
    db.commit()
    db.refresh(ticket)
    return ticket


# delete ticket
@router.delete("/tickets/{id}")
def delete_ticket(
    id: int,
    db: Session = Depends(dependencies.get_db),
    user=Depends(dependencies.get_current_user)
):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == id).first()

    if not ticket or ticket.created_by != user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(ticket)
    db.commit()
    return {"message": "Ticket deleted"}