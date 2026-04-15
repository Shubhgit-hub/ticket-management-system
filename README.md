# 🎫 Ticket Management System

A backend-based Ticket Management System built using FastAPI.
This project allows users to register, login, and manage tickets, with a basic admin system.

---

## 🚀 Features

* 👤 User Registration
* 🔐 User Login
* 🎫 Create Tickets
* 📋 View Tickets
* ✏️ Update Tickets
* 🛠️ Admin Controls
* 📦 SQLite Database Integration

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Validation:** Pydantic
* **Server:** Uvicorn

---

## 📁 Project Structure

```
app/
 ├── main.py
 ├── database.py
 ├── models.py
 ├── schemas.py
 ├── auth.py
 ├── dependencies.py
 └── routers/
      ├── auth.py
      ├── tickets.py
      └── admin.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/ticket-management-system.git
cd ticket-management-system
```

---

### 2️⃣ Create virtual environment (optional but recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run the server

```
python -m uvicorn app.main:app --reload
```

---

### 5️⃣ Open API Docs


http://127.0.0.1:8000/docs  # IMPORTANT READ CAREFULLY



---

## 🧪 API Endpoints

### 🔹 Auth

* `POST /register` → Register new user
* `POST /login` → Login user

---

### 🔹 Tickets

* `POST /tickets` → Create ticket
* `GET /tickets` → Get all tickets
* `PUT /tickets/{id}` → Update ticket

---

### 🔹 Admin

* `GET /admin/tickets` → View all tickets

---

## 🗄️ Database

* Uses SQLite (`test.db`)
* Tables are auto-created on server start

---

##  Future Improvements

* 🔐 Add JWT Authentication
* 🔑 Password Hashing (Security)
* 🌐 Frontend UI (React / HTML)
* 📊 Filtering & Pagination
* 👑 Role-based Access Control

---

##  How It Works

1. User registers using `/register`
2. User logs in using `/login`
3. User creates and manages tickets
4. Admin can view all tickets

---

## 👨‍💻 Author

* Developed by **Shubham Yadav**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

---
