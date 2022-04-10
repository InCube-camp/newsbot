# Rasa How-Tos

## Pre-requisites
- Python
- Rasa (version - 2.x)
- Any IDE (VSCode)

## Create a Rasa bot
1. Create a folder and `cd` into the folder
2. Run the following command to bootstrap your project 
```zsh
rasa init
```
3. Follow the prompted steps
```
  Folder structure :-

  - actions
    - __init__.py
    - actions.py
  - data
    - nlu.yml
    - rules.yml
    - stories.yml
  - models
  - tests
    - test_stories.yml
  - config.yml
  - credentials.yml
  - domain.yml
  - endpoints.yml
```
4. Modify the default data and code to build your bot
    1. Convert your conversation scenario into *`story`* in `stories.yml`
    2. Add examples for your *intents* in `nlu.yml`
    3. Define *rules*, if you have any, in `rules.yml`
    4. Update `domain.yml` to add/remove all used entries. `intents`, `entities`, `responses`, `actions`, `slots`, `forms` etc.
    5. Write code for *actions*, if you have any, in `actions/<any_file>.py`
    6. Update `config.yml` according to your need or leave it alone (*your call*)


## Train your bot
1. Run the following command to train your project
```zsh
rasa train
```

## Test your bot
1. Run the following command to test your project
```zsh
rasa test
```

## Serve/Deploy your bot
1. Run the following command to run rasa core server
```zsh
rasa run
```
> DO NOT forget to add `--cors` entry
```zsh
rasa run --cors "*"
```
2. Run the following command to run rasa action server (if you have defined custom actions)
```zsh
rasa run actions
```
> DO NOT forget to update `endpoints.yml`
```yml
action_endpoint:
  url: "http://<your server address>/webhook"
  # For example "http://localhost:5055/webhook"
```

## Connect with Rasa UI
1. Rasa has a [Chat widget](https://chat-widget-docs.rasa.com/), we can use.
2. Follow the [link](https://chat-widget-docs.rasa.com/) to get to know about all the attributes
3. Add/update the following entry in `credentials.yml`
```yml
socketio:
  user_message_evt: user_uttered
  bot_message_evt: bot_uttered
  session_persistence: false
```

## Conenct with other messenger apps (Telegram)
1. Create a bot and get credentials
    - Goto [BotFather](https://t.me/botfather)
    - Send `/newbot` to create a new bot
    - Chat with [BotFather](https://t.me/botfather) to give your bot a *name* and an *username*
    - Then, disable privacy mode to send message to your bot
    - In case, when you are lost, just send `/help` to [BotFather](https://t.me/botfather)
2. Collect your *username* and *auhorization token* from [BotFather](https://t.me/botfather)
3. Add/update the following entry in `credentials.yml`
```yml
telegram:
  access_token: "<your authorization token"
  verify: "<your bot username>"
  webhook_url: "https://<your server address>/webhooks/telegram/webhook"
```
4. Now restart your Rasa core server and enjoy with Telegram
