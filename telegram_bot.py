from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from common import detect_intent_text
from dotenv import load_dotenv
import os


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Здравствуйте!")


def echo(bot, update):
    text = update.message.text
    reply, _ = detect_intent_text(project_id, update.message.chat_id, text, "ru")
    bot.send_message(chat_id=update.message.chat_id, text=reply)


if __name__ == "__main__":
    load_dotenv()
    telegram_token = os.getenv("TELEGRAM_API_KEY")
    project_id = os.getenv("GOOGLE_PROJECT_ID")

    updater = Updater(telegram_token)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    updater.start_polling()
