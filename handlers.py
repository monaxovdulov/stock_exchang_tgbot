# handlers.py — «склейка»: валидируем вход, зовём game_engine, отвечаем в чат

from typing import Any
import requests
from tg_api import send_message


def _ctx(ctx: dict[str, Any]) -> tuple[requests.Session, str, int, dict]:
    """Удобная распаковка часто используемых полей контекста."""
    return ctx["session"], ctx["base"], ctx["chat_id"], ctx["state"]

def on_ping(ctx: dict[str, Any]) -> None:
    session, base, chat_id, _ = _ctx(ctx)
    send_message(session, base, chat_id, "pong")