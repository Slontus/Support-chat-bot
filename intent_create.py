import requests
import json
from google.cloud import dialogflow
from dotenv import load_dotenv
import os
#from google.cloud import storage

URL = "https://dvmn.org/media/filer_public/a7/db/a7db66c0-1259-4dac-9726-2d1fa9c44f20/questions.json"


def get_phrases_file(url):
    response = requests.get(url)
    data = response.json()
    with open("data.json", "w") as f:
        json.dump(data, f)


def extract_train_phrases(file):
    with open("data.json") as f:
        intents = json.load(f)
    return intents


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(display_name=display_name, training_phrases=training_phrases, messages=[message])

    intents_client.create_intent(request={"parent": parent, "intent": intent})


if __name__ == '__main__':
    load_dotenv()
    #storage.Client()
    project_id = os.getenv('GOOGLE_PROJECT_ID')

    if not os.path.exists("data.json"):
        get_phrases_file(URL)

    intents = extract_train_phrases("data.json")
    for display_name, phrases in intents.items():
        create_intent(project_id, display_name, phrases['questions'], [phrases['answer']])
