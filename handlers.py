# handlers.py — «склейка»: валидируем вход, зовём game_engine, отвечаем в чат

from typing import Any
import requests
from tg_api import send_message
from ai import aitest
import json
import dotenv
import os


def _ctx(ctx: dict[str, Any]) -> tuple[requests.Session, str, int, dict]:
    """Удобная распаковка часто используемых полей контекста."""
    return ctx["session"], ctx["base"], ctx["chat_id"], ctx["state"]

def on_ping(ctx: dict[str, Any]) -> None:
    session, base, chat_id, _ = _ctx(ctx)
    send_message(session, base, chat_id, "pong")
    
def on_help(ctx: dict[str, Any]) -> None:
    session, base, chat_id, _ = _ctx(ctx)
    send_message(session, base, chat_id, "Write to @kalizeev, and describe your problem")

def idk_cmd(ctx: dict[str, Any]) -> None:
    session, base, chat_id, _ = _ctx(ctx)
    send_message(session, base, chat_id, "command not found")

def idk_txt(ctx: dict[str, Any]) -> None:
    session, base, chat_id, _ = _ctx(ctx)
    send_message(session, base, chat_id, "what do you mean")

def aitest1(ctx: dict[str, Any], promt) -> None:
    session, base, chat_id, _ = _ctx(ctx)
    i=aitest(promt)
    send_message(session, base, chat_id, i)