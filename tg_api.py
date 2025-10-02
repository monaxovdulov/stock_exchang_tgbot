# tg_api.py — только HTTP-вызовы к Telegram Bot API

from typing import Any
import requests

def get_updates(
    session: requests.Session,
    base: str,
    offset: int | None,
    timeout_s: int = 30,
) -> list[dict]:
    """
    Вызывает getUpdates. Если offset=None — заберём все накопившиеся апдейты (до лимита).
    timeout_s — сервер будет держать соединение до N секунд (long-poll).
    """
    
    

def send_message(
    session: requests.Session,
    base: str,
    chat_id: int,
    text: str,
) -> None:
    pass