# Ticket Management System

This is a simple Ticket Management System built using FastAPI. It allows users to create and manage tickets, while admins can manage all tickets and view stats.

---

## Features

- User registration and login
- JWT authentication
- Role-based access (User and Admin)
- Create, update, and delete tickets
- Filter tickets by status and priority
- Admin APIs for all tickets and statistics

---

## Tech Stack

- Python (FastAPI)
- SQLite
- SQLAlchemy
- JWT (Authentication)
- Docker

---

## Project Structure

app/
  main.py  
  auth.py  
  database.py  
  models.py  
  schemas.py  
  dependencies.py  
  routers/  
    auth.py  
    tickets.py  
    admin.py  

frontend/  
  index.html  

---

## How to Run

1. Install dependencies

pip install -r requirements.txt

2. Run the server

python -m uvicorn app.main:app --reload

3. Open in browser

http://127.0.0.1:8000

Swagger Docs:

http://127.0.0.1:8000/docs

---

## API Endpoints

### Auth
POST /api/v1/auth/register  
POST /api/v1/auth/login  

### Tickets
POST /api/v1/tickets  
GET /api/v1/tickets  
GET /api/v1/tickets/{id}  
PUT /api/v1/tickets/{id}  
PATCH /api/v1/tickets/{id}/status  
DELETE /api/v1/tickets/{id}  

### Admin
GET /api/v1/admin/tickets  
GET /api/v1/admin/stats  

---

## Notes

- Users can only access their own tickets  
- Admin can access all tickets  
- Passwords are stored in hashed format  
- All protected routes require authentication  

---

## Docker

Build image:

docker build -t ticket-system .

Run container:

docker run -p 8001:8000 ticket-system

---

## Author

Shubham Yadav  
https://github.com/Shubhgit-hub
