# router.py — разбираем update и зовём нужный обработчик

from typing import Any
import requests
import handlers

def handle(update: dict[str, Any], session: requests.Session, base: str, state: dict) -> None:
    """
    Разбирает JSON-представление update.
    Вызывает нужный обработчик для этого update.
    """
    