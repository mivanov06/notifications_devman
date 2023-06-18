import logging
from time import sleep

import requests
from telegram import Bot
from environs import Env

logger = logging.getLogger(__name__)


def get_messages_text(attempts):
    messages_text = []
    for attempt in attempts:
        lesson_title = attempt['lesson_title']
        lesson_url = attempt['lesson_url']
        if attempt['is_negative']:
            text_result = 'К сожалению, в работе нашлись ошибки'
        else:
            text_result = 'Преподователю все понравилось, можно приступить к следующему уроку!'

        message_text = f"У вас проверили работу «{lesson_title}»\n" \
               f"\n" \
               f"{text_result}\n" \
               f"{lesson_url}"
        messages_text.append(message_text)
    return messages_text


def main(devman_token: str, telegram_token: str, chat_id: str):
    bot = Bot(token=telegram_token)
    logger.info("Бот запущен")

    url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': f'Token {devman_token}'
    }
    params = {}

    while True:
        try:
            response = requests.get(url, params=params, headers=headers, timeout=90)
            response.raise_for_status()
        except requests.exceptions.ReadTimeout:
            logger.info('Тайм-аут')
            continue
        except requests.exceptions.ConnectionError:
            logger.info('Соединение потеряно')
            sleep(60)
            continue

        result = response.json()
        if result['status'] == 'timeout':
            params = {
                'timestamp': result['timestamp_to_request']
            }
            logger.info(f"Timeout {result['timestamp_to_request']=}")
        if result['status'] == 'found':
            params = {
                'timestamp': result['last_attempt_timestamp']
            }
            for message_text in get_messages_text(result['new_attempts']):
                bot.send_message(chat_id=chat_id, text=message_text)
                logger.info('Сообщение отправлено')


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    env = Env()
    env.read_env()
    devman_token = env("DEVMAN_TOKEN")
    telegram_token = env("TELEGRAM_TOKEN")
    chat_id = env("CHAT_ID")

    try:
        main(devman_token, telegram_token, chat_id)
    except (KeyboardInterrupt, SystemExit):
        logger.error("Бот остановлен")
