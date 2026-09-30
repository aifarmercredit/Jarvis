from secrets import token_urlsafe
from datetime import datetime, timedelta, timezone

class ConfirmationManager:
    def __init__(self, ttl_seconds: int = 300):
        self._pending = {}
        self.ttl = ttl_seconds

    def create(self, action: str) -> str:
        token = token_urlsafe(24)
        self._pending[token] = (action, datetime.now(timezone.utc) + timedelta(seconds=self.ttl))
        return token

    def consume(self, token: str, action: str) -> bool:
        item = self._pending.pop(token, None)
        if not item:
            return False
        expected, expires = item
        return expected == action and datetime.now(timezone.utc) < expires
