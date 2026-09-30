from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

@dataclass
class Task:
    id: str
    title: str
    completed: bool
    created_at: str

class TaskStore:
    def __init__(self):
        self._items: list[Task] = []

    def add(self, title: str) -> dict:
        task = Task(str(uuid4()), title, False, datetime.now(timezone.utc).isoformat())
        self._items.append(task)
        return task.__dict__

    def list(self) -> list[dict]:
        return [task.__dict__ for task in self._items]
