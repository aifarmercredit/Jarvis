import httpx
from app.ai.provider import AIProvider, AIResponse
from app.core.config import settings

class OpenAICompatibleProvider(AIProvider):
    def __init__(self):
        if not settings.ai_api_key or not settings.ai_model:
            raise ValueError("AI_API_KEY and AI_MODEL are required")
        self.base_url = "https://api.openai.com/v1"
        self.api_key = settings.ai_api_key
        self.model = settings.ai_model

    async def generate(self, messages, tools=None, stream=False):
        if stream:
            raise NotImplementedError("Streaming adapter is not enabled in this provider yet")
        payload = {"model": self.model, "messages": messages}
        if tools:
            payload["tools"] = tools
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(f"{self.base_url}/chat/completions", json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
        choice = data["choices"][0]
        message = choice["message"]
        return AIResponse(content=message.get("content", ""), tool_calls=message.get("tool_calls", []))
