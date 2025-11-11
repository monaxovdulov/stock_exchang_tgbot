# run.py — точка входа: проверяем токен, создаём Session и запускаем поллер

import os
import logging
import requests
from poller import run_loop
import dotenv


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def main() -> None:
    dotenv.load_dotenv()
    token = os.getenv("BOT_TOKEN")
    

    base_url = f"https://api.telegram.org/bot{token}"

    # Один Session на всё приложение — быстрее и проще
    with requests.Session() as session:
        session.headers.update({"User-Agent": "exchange-bot/0.1"})
        run_loop(session, base_url)


if __name__ == "__main__":
    main()
