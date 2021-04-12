# Support chat bot

This is a simple telegram and vk chat bots integrated with google 
dialogflow agent

### How to Install

Python3 should be already installed. Then use pip (or pip3,
if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
To run this program you need to create **.env** with the following structure:
```buildoutcfg
TELEGRAM_API_KEY=your telegram bot API key
GOOGLE_PROJECT_ID=your google project identificator
GOOGLE_APPLICATION_CREDENTIALS=path to your Google APU authentication credentials JSON file
VK_ACCESS_TOKEN=your VK access token
```
To create telegram bot write to [Bot Father](https://telegram.me/BotFather)

Here you can create [Google DialogFlow project](https://cloud.google.com/dialogflow/es/docs/quick/setup)

Here you can create [DialogFlow agent](https://cloud.google.com/dialogflow/es/docs/quick/build-agent)

Step list to create Google authentication [JSON-key](https://cloud.google.com/docs/authentication/getting-started)

If you need integration with VK, create new group in 
[Managed communities](https://vk.com/groups?tab=admin).
You will receive access token in the setting of your group (API usage tab).
Also, you will need to enable community messages.

To train your DialogFlow agent you need to create intents for every specific scenario.
You can create intents manually or use a `intent_create.py` 
to upload them through DialogFlow API.
In the later case you need to create `data.json` file in the project directory with 
the following structure:

```json
{
    "Your intent 1 name": {
        "questions": [
            "Possible question 1",
            "Possible question 2",
            ...
            "Possible question n"
        ],
        "answer": "Provide your answer here"
    },
    ...
}
```

### Project Goals
The code is written for educational purposes on online-course 
for web-developers [dvmn.org](https://dvmn.org).