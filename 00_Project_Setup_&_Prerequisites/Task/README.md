# **🚀 Mini Task: Create a FastAPI Project and Run a Simple API**

## **Step 1: Create a New FastAPI Project**

First, navigate to a directory where you want to create your project and run:

```bash
mkdir fastapi_project && cd fastapi_project
```

---

## **Step 2: Activate the Virtual Environment**

If not activated, do so now:

**Windows (Command Prompt / PowerShell)**

```powershell
fastapi_env\Scripts\activate
```

**Linux/macOS (Terminal)**

```bash
source fastapi_env/bin/activate
```

---

## **Step 3: Install FastAPI and Uvicorn**

Ensure you have **FastAPI and Uvicorn** installed inside the virtual environment:

```bash
pip install fastapi uvicorn
```

---

## **Step 4: Create `main.py` (Basic API)**

Create a new file **`main.py`** in your project folder and add the following code:

```python
from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Define a basic endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Another example endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
```

> **Explanation:**

- `@app.get("/")` → A **GET request** to the root (`/`) returns a simple message.
- `@app.get("/items/{item_id}")` → Fetches an item by **ID** and an optional **query parameter (`q`)**.

---

## **Step 5: Run the FastAPI Application**

Use **Uvicorn** to start the FastAPI server:

```bash
uvicorn main:app --reload
```

> **Expected Output:**

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

---

## **Step 6: Test the API Endpoints**

Now, open a browser or **Postman** and test:

1. **Test Root Endpoint:**

- URL: **`http://127.0.0.1:8000/`**
- Expected Response:

```json
{ "message": "Hello, FastAPI!" }
```

2. **Test Dynamic Route:**

- URL: **`http://127.0.0.1:8000/items/5?q=fastapi`**
- Expected Response:

```json
{
  "item_id": 5,
  "query": "fastapi"
}
```

3. **Access the Interactive API Docs:**  
   FastAPI provides **automatic documentation**:

- **Swagger UI:** [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)
- **ReDoc UI:** [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc)

---

### **Mini Task Complete!**

**You have successfully set up and run a FastAPI project** 🎉
