# tg_api.py — только HTTP-вызовы к Telegram Bot API

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
    params = {"timeout": timeout_s, "offset": offset}
    response = session.get(
        base + "/getUpdates", params=params, timeout=(5, timeout_s + 5)
    )
    response.raise_for_status()
    data = response.json()
    return data["result"]


def send_message(
    session: requests.Session,
    base: str,
    chat_id: int,
    text: str,
) -> None:
    payload = {"chat_id": chat_id, "text": text}
    response = session.post(base + "/sendMessage", json=payload)
    response.raise_for_status()
