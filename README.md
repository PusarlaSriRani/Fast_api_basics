# 🚀 FastAPI Basics

A beginner-friendly FastAPI project demonstrating the fundamentals of building REST APIs using Python and FastAPI. This repository contains simple examples of GET, POST, PUT, DELETE, Login, List, and Calculator APIs to understand backend development concepts.

---

## 📌 Project Overview

This project is designed to learn and practice FastAPI by implementing commonly used API operations. Each file demonstrates a specific concept with clean and easy-to-understand code.

---


## 🛠️ Technologies Used

* Python 3.x
* FastAPI
* Pydantic
* Uvicorn

---

## 📚 Concepts Covered

### 1. FastAPI

FastAPI is a modern, high-performance Python web framework used for building REST APIs quickly with automatic documentation and data validation.

---

### 2. GET API

Retrieves data from the server without modifying it.

**Example**

```
GET /students
```

---

### 3. POST API

Sends new data from the client to the server.

**Example**

```
POST /student-info
```

---

### 4. PUT API

Updates existing data on the server.

**Example**

```
PUT /student/1
```

---

### 5. DELETE API

Removes existing data from the server.

**Example**

```
DELETE /student/1
```

---

### 6. Path Parameters

Accept values directly from the URL.

Example:

```
/student/101
```

---

### 7. Query Parameters

Pass values through the URL.

Example:

```
/search?name=Sri&age=21
```

---

### 8. Pydantic Models

Used for request validation and automatic type checking.

Example:

```python
class StudentRequest(BaseModel):
    name: str
    age: int
    city: str
```

---

### 9. JSON Response

FastAPI automatically converts Python dictionaries into JSON responses.

Example:

```json
{
    "name": "Sri Rani",
    "age": 21,
    "city": "Hyderabad"
}
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/PusarlaSriRani/Fast_api_basics.git
```

Navigate to the project folder:

```bash
cd Fast_api_basics
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run the application:

```bash
uvicorn hello_world:app --reload
```

---

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 🔄 Request–Response Lifecycle

```
Client
   │
   ▼
HTTP Request
   │
   ▼
FastAPI Route
   │
   ▼
Pydantic Validation
   │
   ▼
Business Logic
   │
   ▼
Response Generation
   │
   ▼
JSON Response
   │
   ▼
Client
```

---

## 🎯 Learning Outcomes

By completing this project, you will understand:

* FastAPI application structure
* REST API development
* GET, POST, PUT, and DELETE methods
* Path and Query Parameters
* Request Body Validation using Pydantic
* JSON Request and Response handling
* Interactive API documentation
* Basic backend development workflow

---
