from app.ai.provider import AIProvider
from app.ai.http_provider import OpenAICompatibleProvider
from app.core.config import settings

class ModelManager:
    def __init__(self, provider: AIProvider | None = None):
        if provider is not None:
            self.provider = provider
        elif settings.ai_api_key and settings.ai_model:
            self.provider = OpenAICompatibleProvider()
        else:
            self.provider = None

    @property
    def available(self) -> bool:
        return self.provider is not None
