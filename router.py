# router.py — разбираем update и зовём нужный обработчик

from typing import Any
import requests
import handlers


def handle(
    update: dict[str, Any], session: requests.Session, base: str, state: dict
) -> None:
    """
    Разбирает JSON-представление update.
    Вызывает нужный обработчик для этого update.
    """

    if "message" in update:
        msg = update["message"]
        text = msg.get("text").strip()
        if text == "/ping":
            ctx = {
                "session": session,
                "base": base,
                "state": state,
                "chat_id": msg["chat"]["id"],
                "user_id": msg["from"]["id"],
                "username": msg["from"].get("username"),
                "message_id": msg["message_id"],
                "args": text.split(),
            }
            handlers.on_ping(ctx)
        elif text == "/help":
            ctx = {
                "session": session,
                "base": base,
                "state": state,
                "chat_id": msg["chat"]["id"],
                "user_id": msg["from"]["id"],
                "username": msg["from"].get("username"),
                "message_id": msg["message_id"],
                "args": text.split(),
            }
            handlers.on_help(ctx)
    else:
        return None
