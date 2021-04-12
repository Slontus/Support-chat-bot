from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from common import detect_intent_text
from google.cloud import storage
from dotenv import load_dotenv
import os


'''
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm stupid bot!")
'''


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm stupid bot!")


'''
def echo(update, context):
    text = update.message.text
    reply, _ = detect_intent_text(project_id, update.effective_chat.id, text, "ru")
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
'''
def echo(bot, update):
    text = update.message.text
    reply, _ = detect_intent_text(project_id, update.message.chat_id, text, "ru")
    bot.send_message(chat_id=update.message.chat_id, text=reply)

'''
def detect_intent_text(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)

    return response.query_result.fulfillment_text
'''

if __name__ == "__main__":
    load_dotenv()
    telegram_token = os.getenv("TELEGRAM_API_KEY")
    project_id = os.getenv("GOOGLE_PROJECT_ID")
    storage.Client()

    updater = Updater(telegram_token)
    #updater = Updater(telegram_token, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    updater.start_polling()
