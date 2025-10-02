# poller.py — бесконечный цикл: забираем апдейты, обрабатываем, сохраняем state и offset

import time
import logging
from typing import Any
import requests
from tg_api import get_updates
from router import handle


log = logging.getLogger(__name__)

def run_loop(session: requests.Session, base_url: str) -> None:
    """
    Главный цикл:
    - читаем state и offset;
    - long-poll getUpdates;
    - каждый апдейт отдаём в router.handle;
    - после успешной обработки: сохраняем state, затем offset = update_id + 1;
    - повторяем.
    """