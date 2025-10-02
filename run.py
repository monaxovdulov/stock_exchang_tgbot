# run.py — точка входа: проверяем токен, создаём Session и запускаем поллер

import os
import sys
import logging
import requests
from poller import run_loop
from storage import ensure_data_dir

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def main() -> None:
    token = os.environ.get("BOT_TOKEN")
    if not token:
        logging.error("Переменная окружения BOT_TOKEN не установлена.")
        sys.exit(1)

    base_url = f"https://api.telegram.org/bot{token}"
    ensure_data_dir()

    # Один Session на всё приложение — быстрее и проще
    with requests.Session() as session:
        session.headers.update({"User-Agent": "exchange-bot/0.1"})
        run_loop(session, base_url)

if __name__ == "__main__":
    main()
