from uuid import uuid4
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.core.assistant import Assistant
from app.core.memory import MemoryStore
from app.core.tasks import TaskStore

router = APIRouter()
assistant = Assistant()
memory = MemoryStore()
tasks = TaskStore()

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=20000)
    conversation_id: str | None = None

class MemoryRequest(BaseModel):
    content: str = Field(min_length=1, max_length=5000)

class TaskRequest(BaseModel):
    title: str = Field(min_length=1, max_length=500)

@router.get("/health")
async def health():
    return {"status": "healthy", "ai": assistant.provider_available, "database": False, "voice": False, "web_search": False}

@router.post("/chat")
async def chat(request: ChatRequest):
    request_id = str(uuid4())
    try:
        result = await assistant.respond(request.message, conversation_id=request.conversation_id)
        return {"success": True, "request_id": request_id, "type": "assistant_response", **result}
    except Exception as exc:
        raise HTTPException(status_code=503, detail={"code": "ASSISTANT_ERROR", "message": str(exc)})

@router.get("/memory")
async def get_memory():
    return {"success": True, "items": memory.list()}

@router.post("/memory")
async def add_memory(request: MemoryRequest):
    return {"success": True, "memory": memory.add(request.content)}

@router.delete("/memory")
async def clear_memory():
    memory.clear()
    return {"success": True}

@router.get("/tasks")
async def get_tasks():
    return {"success": True, "items": tasks.list()}

@router.post("/tasks")
async def add_task(request: TaskRequest):
    return {"success": True, "task": tasks.add(request.title)}
