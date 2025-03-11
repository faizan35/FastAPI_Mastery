from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

task = []

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

app.post("/task/", response_model=Task)
def create_task(task: Task):
    task.append(task)
    return task

@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return {"error": "Task not found"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = task_update
            return task_update
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": f"Task {task_id} deleted"}

# Run with: uvicorn main:app --reload