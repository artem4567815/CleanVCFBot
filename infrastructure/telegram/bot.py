import os
import tempfile
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from config import BOT_TOKEN, SUPPORTED_EXTENSIONS, MAX_FILE_SIZE_MB
from logger import logger
from app.services.import_service import ImportContactsService
from aiogram import Router
import asyncio

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)
svc = ImportContactsService()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    try:
        await message.answer(
            "Отправьте файл с номерами телефонов (.txt, .doc, .docx, .xlsx).\n"
            "Я очищу их, приведу к формату +7XXXXXXXXXX, удалю дубликаты и пришлю .vcf для импорта."
        )
    except Exception as e:
        logger.error(f"Ошибка в обработчике /start: {e}")



@router.message(lambda msg: msg.document)
async def handle_doc(message: types.Message):
    try:
        doc = message.document
        file_id = doc.file_id
        ext = os.path.splitext(doc.file_name)[-1].lower()
        if ext not in SUPPORTED_EXTENSIONS:
            await message.reply(f"Формат {ext} не поддерживается.")
            return
        if doc.file_size > MAX_FILE_SIZE_MB * 1024 * 1024:
            await message.reply("Файл слишком большой.")
            return

        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, doc.file_name)
            await bot.download(file_id, destination=file_path)
            try:
                vcf_path = svc.import_and_generate_vcf(file_path, tmpdir)
                await message.reply_document(document=FSInputFile(vcf_path), caption="Ваши контакты:")
            except Exception as e:
                logger.error(f"Ошибка обработки файла: {e}")
                await message.reply("Произошла ошибка обработки файла.")
    except Exception as e:
        logger.error(f"Ошибка в обработчике handle_doc: {e}")
        await message.reply("Произошла внутренняя ошибка.")

@router.message(lambda msg: not msg.document and msg.text != "/start")
async def handle_non_doc(message: types.Message):
    try:
        await message.reply("Я работаю только с документами. Пожалуйста, отправьте файл для обработки.")
    except Exception as e:
        logger.error(f"Ошибка в обработчике handle_non_doc: {e}")

def run_bot():
    try:
        asyncio.run(dp.start_polling(bot))
    except Exception as e:
        logger.error(f"Ошибка запуска бота: {e}")
