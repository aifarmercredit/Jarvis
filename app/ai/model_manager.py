from app.ai.provider import AIProvider

class ModelManager:
    def __init__(self, provider: AIProvider | None = None):
        self.provider = provider

    @property
    def available(self) -> bool:
        return self.provider is not None
