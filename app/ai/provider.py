from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, AsyncIterator

@dataclass
class AIResponse:
    content: str
    tool_calls: list[dict[str, Any]]

class AIProvider(ABC):
    @abstractmethod
    async def generate(self, messages: list[dict[str, str]], tools: list[dict] | None = None, stream: bool = False) -> AIResponse | AsyncIterator[str]:
        raise NotImplementedError
