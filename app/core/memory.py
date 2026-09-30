from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

@dataclass
class Memory:
    id: str
    content: str
    created_at: str

class MemoryStore:
    def __init__(self):
        self._items: list[Memory] = []

    def add(self, content: str) -> dict:
        item = Memory(str(uuid4()), content, datetime.now(timezone.utc).isoformat())
        self._items.append(item)
        return item.__dict__

    def list(self) -> list[dict]:
        return [item.__dict__ for item in self._items]

    def clear(self) -> None:
        self._items.clear()
