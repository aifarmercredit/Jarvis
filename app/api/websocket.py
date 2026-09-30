from fastapi import WebSocket, WebSocketDisconnect
from app.core.assistant import Assistant

assistant = Assistant()

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            message = data.get("message")
            if not isinstance(message, str) or not message.strip():
                await websocket.send_json({"event": "assistant_error", "error": {"code": "INVALID_INPUT"}})
                continue
            await websocket.send_json({"event": "assistant_start", "state": "THINKING"})
            result = await assistant.respond(message)
            await websocket.send_json({"event": "assistant_complete", "state": result["state"], "content": result["content"]})
    except WebSocketDisconnect:
        return
