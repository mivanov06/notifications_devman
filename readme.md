# Бот для отправки уведомлений о проверке работ на сайте dvmn.org

Позволяет получать уведомления о проверке работ через Telegram бота

Для работы скрипта должен быть уже установлен`python3`. 

## Установка:

1. Скачайте репозиторий и распакуйте.
2. Используйте виртуальное окружение для установки пакетов

```
python -m env env
```
```
env\bin\activate
```

4. Установите пакеты командой 

  ```
  pip install -r requirements.txt
  ``` 
5. Создайте в корне репозиторя файл `.env` со следующими строками:

```
DEVMAN_TOKEN=токен Devman
TELEGRAM_TOKEN=токен Telegram бота
CHAT_ID=ваш chat_id Telegram

TELEGRAM_LOGGER_TOKEN=токен Telegram бота для отправки логов админу
CHAT_ADMIN_ID=chat_id админа
```
Персональный токен можно получить, на сайте [Девман](https://dvmn.org/api/docs/).  
Создать бота для Telegram и узнать его токен можно у [BotFather](https://telegram.me/BotFather).  
Сhat_id можно получить у [userinfobot](https://telegram.me/userinfobot).

## Запуск:

Запуск скрипта производится командой 
```
python main.py
```

###  Для запуска контейнера Docker:

Должен быть установлен `docker` и `docker-compose`

1. Создайте контейнер командой
```
docker build -f dockerfile . -t devman_bot
```

2. Запустите контейнер командой
```
docker-compose run --rm -d bot
```

3. Для остановки используйте
```
docker stop container_id
```

`container_id` можно узнать с помощью команды

```
docker container ls
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).