from uuid import uuid4
from app.ai.model_manager import ModelManager
from app.core.personality import SYSTEM_PERSONALITY
from app.core.context import ConversationContext

class Assistant:
    def __init__(self, model_manager: ModelManager | None = None):
        self.model_manager = model_manager or ModelManager()
        self._sessions: dict[str, ConversationContext] = {}

    @property
    def provider_available(self) -> bool:
        return self.model_manager.available

    async def respond(self, message: str, conversation_id: str | None = None) -> dict:
        cid = conversation_id or str(uuid4())
        ctx = self._sessions.setdefault(cid, ConversationContext(cid))
        ctx.add("user", message)
        if not self.provider_available:
            content = "JARVIS AI is not configured yet. Add your AI provider settings to .env."
            ctx.add("assistant", content)
            return {"content": content, "state": "IDLE", "tool_calls": [], "conversation_id": cid}
        messages = [{"role": "system", "content": SYSTEM_PERSONALITY}, *ctx.recent()]
        response = await self.model_manager.provider.generate(messages)
        ctx.add("assistant", response.content)
        return {
            "content": response.content,
            "state": "IDLE",
            "tool_calls": response.tool_calls,
            "conversation_id": cid,
        }
