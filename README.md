Course: WebSovellusKehitys – Autumn 2025
Project: Car Rental Web Application (Angular + Flask + SQLite + Docker)
Author: **Oleg Shaltaev**

This section provides all necessary information for evaluating the project according to the course requirements.
It includes access to the deployed application, API testing instructions, repository link, architecture overview, and technical notes.

---

# ✅ **📌 Project Links**

### **🔗 Live Demo (Frontend + Backend API)**

**[https://car-rental-fullstack-7gx6.onrender.com](https://car-rental-fullstack-7gx6.onrender.com)**

Accessible publicly, no login required.
Opens the Angular Single Page Application and communicates with the Flask backend.

### **🔗 GitHub Repository**

[https://github.com/oshaltaev-1995/car-rental-fullstack](https://github.com/oshaltaev-1995/car-rental-fullstack)

---

# 🧱 **📌 Architecture Overview**

This project implements a complete **full-stack web application** following modern development practices:

### **Frontend**

* Angular SPA
* Routed pages
* REST API integration
* Production build delivered via Docker

### **Backend**

* Python + Flask
* REST API
* CORS enabled
* Persistent relational database (SQLite)
* Gunicorn WSGI server for production

### **Data Persistence**

* SQLite database stored inside container:

  ```
  backend/data/orders.db
  ```
* Automatically initialized on first startup
* Satisfies the course requirement for using a relational or document database

### **Deployment**

* Docker multi-stage build (Node + Python)
* Single-container deployment (microservice single-unit model)
* Hosted on Render Web Service
* Publicly available for testing

---

# 🧪 **📌 API Testing Instructions**

The backend exposes a simple REST API for submitting and retrieving rental orders.

---

## **1. Create a new rental order**

`POST /api/order`

### Example:

```bash
curl -X POST https://car-rental-fullstack-7gx6.onrender.com/api/order \
  -H "Content-Type: application/json" \
  -d '{"car":"BMW M5","name":"Test User","phone":"123456"}'
```

### Expected Response:

```json
{
  "message": "Your order has been saved!"
}
```

This confirms the backend, database, routing, and deployment are all functioning.

---

## **2. Retrieve all orders**

`GET /api/orders`

```bash
curl https://car-rental-fullstack-7gx6.onrender.com/api/orders
```

Example response:

```json
[
  {
    "id": 1,
    "car": "BMW M5",
    "name": "Test User",
    "phone": "123456",
    "timestamp": "2025-11-14T14:48:00"
  },
  ...
]
```

This demonstrates:

* database storage
* SELECT queries
* JSON serialization
* REST endpoint design

---

# 🐳 **📌 Docker Deployment Summary**

The application is packaged using a **multi-stage Dockerfile**:

1. Stage 1 — Angular production build (Node)
2. Stage 2 — Flask backend + SQLite + compiled frontend (Python)
3. Served via Gunicorn on port 5000
4. Render automatically builds & deploys container on every Git push

This matches modern cloud deployment practices.

---

# 🎯 **📌 Course Learning Objective Alignment**

This project demonstrates all key objectives:

### ✔ Full-stack development (UI + backend + persistence)

### ✔ REST API creation

### ✔ Microservice-style containerization (single-service Docker)

### ✔ Use of a relational database (SQLite)

### ✔ Deployment to cloud environment

### ✔ Use of modern JavaScript framework (Angular)

### ✔ Use of Python backend for API logic

### ✔ Proper documentation & API testing