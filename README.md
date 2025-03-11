# FastAPI Mastery Roadmap (With Projects)

## **Module 0: Project Setup & Prerequisites**

### **[0.1 Understanding FastAPI & Use Cases](./00_Project_Setup_&_Prerequisites/0.1_Understanding_FastAPI_Use_Cases.md)**

- What is FastAPI?
- How FastAPI compares to Flask & Django
- FastAPI use cases & real-world examples

### **[0.2 Setting Up Development Environment](./00_Project_Setup_&_Prerequisites/0.2_Setting_Up_Development_Environment.md)**

- **Installing Python (Windows/Linux/macOS)**
- **Setting up Virtual Environment (venv)**

- Windows: `python -m venv fastapi_env`
- Linux/macOS: `python3 -m venv fastapi_env`

### **[0.3 Web Servers & ASGI vs WSGI & Uvicorn vs Gunicorn](./00_Project_Setup_&_Prerequisites/0.3_Web_Servers.md)**

- **Introduction to Web Servers & Their Need in FastAPI**
- **WSGI vs ASGI: Understanding the Core Differences**
- **Uvicorn: The Preferred ASGI Server for FastAPI**
- **Gunicorn vs Uvicorn: When & Why to Use Each**
- **Alternative ASGI Servers & Deployment Considerations**

### **[0.4 Installing FastAPI with Uvicorn (default) & Uvicorn + Gunicorn (combined)](./00_Project_Setup_&_Prerequisites/0.4_Installing_FastAPI.md)**

- **Installing FastAPI & Web Servers (Uvicorn and Gunicorn)**
- **Setting Up a Simple FastAPI App**
- **Running FastAPI with Uvicorn (Default Setup)**
  - Starting the FastAPI app with Uvicorn
  - Configuring host, port, and reload options
  - Running with multiple workers
- **Running FastAPI with Gunicorn + Uvicorn (Production Setup)**
  - Installing Gunicorn
  - Running FastAPI with Gunicorn and Uvicorn workers
  - Configuring worker count and process management
- **Performance Considerations & Best Practices**
- **Deploying FastAPI with Docker**

### **[0.5 Essential Development Tools](./00_Project_Setup_&_Prerequisites/0.5_Tools_and_extensions.md)**

- Postman, SQLite/PostgreSQL clients
- VS Code / PyCharm Setup
- Debugging Extensions

#### **[Mini Task:](./00_Project_Setup_&_Prerequisites/Task/README.md)**

- **Create a FastAPI project and run a simple API**

## **Module 1: FastAPI Basics - Building REST APIs**

### **[1.1 FastAPI Core Concepts](./01_FastAPI_Basics/1.1_FastAPI_core_Concepts.md)**

- Request & Response Cycle
- Path Operations (`@app.get()`, `@app.post()`, `@app.put()`, `@app.delete()`)
- Query Parameters, Path Parameters

### **[1.2 Data Handling with Pydantic](./01_FastAPI_Basics/1.2_Data_Handling_with_Pydantic.md)**

- Using **Pydantic Models** for request validation
- Response models & Field validation
- Using `Optional[]` for optional fields

### **[1.3 Handling Request Body & Form Data](./01_FastAPI_Basics/1.3_Handling_Request_Body_Form_Data.md)**

- Sending JSON data in requests
- Form data & File uploads

#### **[Mini Project:](./01_FastAPI_Basics/Task/README.md)**

1. **Simple To-Do API** (Basic CRUD operations)
2. **Form that has single file upload and multiple file upload features.**

## **Module 2: Working with Databases (SQL & NoSQL)**

**(Duration: 1 Week)**

### **2.1 Connecting to Databases**

- SQLAlchemy with PostgreSQL/MySQL
- SQLite for local development
- MongoDB with Motor (Async DB)

### **2.2 Defining Database Models**

- ORM Models using SQLAlchemy
- Creating tables & migrations

### **2.3 Performing CRUD Operations**

- Querying data using SQLAlchemy ORM
- Creating, updating, deleting records

#### **Mini Project:**

- **Bookstore API** (Books, Authors, Reviews CRUD with PostgreSQL)

---

## **Module 3: Authentication & Authorization**

**(Duration: 1 Week)**

### **3.1 User Authentication with OAuth2 & JWT**

- OAuth2 with Password Flow
- JWT Tokens (Login, Refresh Tokens)

### **3.2 Password Hashing & User Management**

- Using `passlib` for password hashing
- Storing hashed passwords securely

### **3.3 Role-Based Access Control (RBAC)**

- Defining user roles (Admin, User)
- Restricting endpoints based on roles

#### **Mini Project:**

- **User Authentication API (JWT-based Login & Signup)**

---

## **Module 4: Background Tasks, Middleware & Caching**

**(Duration: 1 Week)**

### **4.1 Background Tasks in FastAPI**

- Running async tasks in background
- Use cases (sending emails, reports)

### **4.2 Middleware in FastAPI**

- Custom middleware for request logging
- Modifying requests and responses

### **4.3 Caching Responses & Rate Limiting**

- Using **Redis** for caching API responses
- Implementing **Rate Limiting** for APIs

#### **Mini Project:**

- **File Upload & Processing API (With Background Tasks)**

---

## **Module 5: WebSockets & Real-time Communication**

**(Duration: 1 Week)**

### **5.1 WebSockets in FastAPI**

- Setting up WebSocket connections
- Handling real-time messages

### **5.2 Implementing Real-time Notifications**

- WebSocket-based live updates
- Broadcasting messages to multiple clients

#### **Mini Project:**

- **Real-time Chat App (WebSocket-based Chat System)**

---

## **Module 6: API Testing & Documentation**

**(Duration: 1 Week)**

### **6.1 Writing Unit & Integration Tests**

- Using `pytest` for API testing
- Testing endpoints with `httpx`

### **6.2 FastAPI Interactive Documentation**

- Using **Swagger UI** & **Redoc**
- Customizing OpenAPI schema

#### **Mini Project:**

- **Test-Driven API (Fully Tested API with Pytest)**

---

## **Module 7: Deployment, CI/CD & Scalability**

**(Duration: 1 Week)**

### **7.1 Dockerizing FastAPI Applications**

- Creating Dockerfile for FastAPI
- Running FastAPI in Docker

### **7.2 Deploying FastAPI on Cloud**

- Deploying on **AWS/GCP/Azure**
- Using **Gunicorn + Uvicorn** for production

### **7.3 CI/CD for FastAPI**

- Setting up GitHub Actions for CI/CD
- Auto-deploying on Docker/Kubernetes

#### **Final Project:**

- **Production-Ready E-commerce API (Authentication, DB, Caching, Deployment)**

---

# **Capstone Project: Full SaaS API**

**(Bringing all concepts together!)**

### **Project:** **"Complete SaaS API"**

- User Authentication (JWT & OAuth)
- Subscription Management (Stripe API)
- Role-Based Access (Admin/User)
- WebSockets for Notifications
- Async Background Tasks (Emails, Reports)
- Deployment with Docker & Kubernetes

---
