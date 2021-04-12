import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
import os
import random
from common import detect_intent_text


def echo(event, vk_session_api, reply):
    vk_session_api.messages.send(
        user_id=event.user_id,
        message=reply,
        random_id=random.randint(1, 1000)
    )


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("VK_ACCESS_TOKEN")
    project_id = os.getenv("GOOGLE_PROJECT_ID")

    vk_session = vk_api.VkApi(token=token)
    vk_session_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            reply, is_fallback = detect_intent_text(project_id, event.user_id, event.text, 'ru')
            if not is_fallback:
                echo(event, vk_session_api, reply)
