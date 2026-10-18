import asyncio
from telethon import TelegramClient, functions

# 1. Add your API credentials here (get them from https://telegram.org)
API_HASH = "461fce04fe913ad6a433d68f6edccbf3"  
API_ID = 33204279  # Replace with your string API Hash
SESSION_NAME = 'session_contacts_fetcher'

TARGET_USERNAMES = [
    "@s_marguba",
    "@Khasanjonovm ",
    "@GAGERS56"
]


LIMIT = 100 
# ------------------

async def main():
    # Создаем клиента Telegram (файл 'session_name.session' сохранит авторизацию)
    async with TelegramClient('session_name', API_ID, API_HASH) as client:
        print("Авторизация успешна. Начинаем сбор сообщений...\n")
        
        for username in TARGET_USERNAMES:
            print(f"Обработка пользователя: {username}...")
            try:
                # Получаем сущность пользователя (проверка на валидность)
                entity = await client.get_input_entity(username)
                
                # Создаем имя файла для сохранения
                filename = f"chat_{username}.txt"
                
                with open(filename, 'w', encoding='utf-8') as f:
                    # Итерируемся по истории сообщений
                    async for message in client.iter_messages(entity):
                        # Определяем отправителя
                        sender = "Вы" if message.out else username
                        # Берем текст сообщения или описание медиа (если текста нет)
                        text = message.text or "[Медиа/Стикер/Файл]"
                        # Форматируем дату
                        date_str = message.date.strftime('%Y-%m-%d %H:%M:%S')
                        
                        f.write(f"[{date_str}] {sender}: {text}\n")
                        
                print(f"✓ Успешно сохранено в {filename}")
                
            except Exception as e:
                print(f"✗ Ошибка при работе с {username}: {e}")
                
            # Небольшая пауза во избежание флуд-бана от Telegram
            await asyncio.sleep(2)

if __name__ == '__main__':
    # Запуск асинхронного скрипта
    asyncio.run(main())