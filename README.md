**Ticket Management System**

This is a basic ticket management system built using FastAPI. It allows users to create and manage tickets, with separate routes for authentication, admin, and ticket operations.

Features
User authentication (login/signup)
Create and manage tickets
Admin-related functionality
Simple frontend (HTML)
FastAPI backend
Docker support
Tech Used
Python (FastAPI)
SQLite database
Uvicorn server
Docker


**Project Structure**
Ticket Management System/

app/
  main.py
  models.py
  schemas.py
  database.py
  auth.py
  dependencies.py
  routers/
    auth.py
    admin.py
    tickets.py

frontend/
  index.html

test.db
requirements.txt
Dockerfile
*How to Run*
Run locally
Install dependencies
pip install -r requirements.txt
Start server
python -m uvicorn app.main:app --reload
Open in browser
http://127.0.0.1:8000

API docs:

http://127.0.0.1:8000/docs
***Run using Docker***

.Build image:

.docker build -t ticket-system .

##Run container:

.docker run -p 8001:8000 ticket-system

Then open:
http://localhost:8001

Notes:-If port 8000 is already in use, change the port while running Docker.
Make sure Docker Desktop is running before building the image.
Author

Shubham Yadav
https://github.com/Shubhgit-hub
