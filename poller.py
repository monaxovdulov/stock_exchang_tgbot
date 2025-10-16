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
    offset = None
    while True:
            updates = get_updates(session, base_url, offset, timeout_s=30)
            if updates==[]:
                continue
            else:
                for update in updates:
                    uid = update["update_id"]
                    handle(update, session, base_url, state={})
                    offset = uid + 1
       # except requests.RequestException:
       #     logging.info("updates=%d offset=%s", len(updates), offset)
       # except UnboundLocalError:
       #     continue