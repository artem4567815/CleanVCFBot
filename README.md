
# CleanVCFBot

CleanVCFBot — это Telegram-бот для обработки и конвертации файлов (.txt, .xlsx, .doc, .docx) с контактами. Бот принимает документы, обрабатывает их и отправляет пользователю результат.

## Стек технологий

- Python 3.11
- [aiogram](https://github.com/aiogram/aiogram) (Telegram Bot API)
- Docker, Docker Compose
- pandas
- python-docx
- phonenumbers
- python-dotenv

## Быстрый старт

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/artem4567815/CleanVCFBot.git
   cd CleanVCFBot
   ```

2. **Создайте файл `.env` и добавьте токен бота:**
   ```
   TOKEN=ваш_токен_бота
   ```

3. **Соберите и запустите контейнер:**
   ```bash
   docker-compose up -d --build
   ```

4. **Использование:**
   - /start
   - Отправьте боту файл.
   - Получите обработанный файл в ответ.

## Запуск без Docker

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Запустите бота:
   ```bash
   python main.py
   ```

