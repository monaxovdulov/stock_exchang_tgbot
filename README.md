```
flowchart TD
  %% Узлы
  subgraph Top[Запуск]
    RUN[run.py - Старт]
  end

  subgraph IO[Внешний мир]
    TGAPI[TG API клиент - tg_api.py]
    STORE[(Хранилище - storage.py\nstate.json и offset.txt)]
    TG[(Telegram Bot API)]
  end

  subgraph APP[Приложение]
    POLL[Поллер - poller.py]
    ROUTE[Роутер - router.py]
    HANDL[Хэндлеры - handlers.py]
    ENGINE[Игровой движок - game_engine.py]
    STATE{{state - dict в памяти}}
    TICK[[tick_timers_if_needed]]
  end

  %% Основной поток
  RUN -->|создает Session и base_url| POLL

  POLL -->|getUpdates: offset + timeout| TGAPI
  TGAPI <--> |HTTP JSON| TG
  TGAPI -->|result: updates| POLL

  POLL -->|router.handle update + ctx| ROUTE
  ROUTE -->|ctx: chat_id + user_id + args| HANDL
  HANDL -->|вызовы правил игры| ENGINE

  HANDL -->|sendMessage / editMessageText / answerCallbackQuery| TGAPI

  %% Сохранения
  HANDL -->|save_state_atomic state| STORE
  POLL -->|save_offset: update_id + 1| STORE

  %% Работа с state в памяти
  POLL -. читает при старте .-> STATE
  HANDL -. читает и меняет .-> STATE
  ENGINE -. меняет .-> STATE

  %% Таймеры
  POLL -->|каждый тик| TICK
  TICK -->|если дедлайн настал| ENGINE

```
