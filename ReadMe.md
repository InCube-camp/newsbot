# NewsBot
> A Rasa Chatbot that keeps user updated of news

## Clone this project
```zsh
git clone https://github.com/InCube-camp/newsbot.git
cd newsbot
```

## Install all dependencies
```zsh
pip install -r requirements.txt --user
```

## Get the `newsapi-python` API key
1. Go to [newsapi.org](https://newsapi.org/)
2. Click on `Get API Key`
3. Then follow the steps to get the API key and put it in environment variable
4. Run the following command to put the API key in environment valiable
```pwsh
# Windows
set NEWSAPI_KEY=#####YOUR API KEY#######
```
```zsh
# Linux / Mac
export NEWSAPI_KEY=#####YOUR API KEY#######
```

## Train the bot
```zsh
rasa train
```

## Run the bot
1. In one command prompt run the following command to run the action server
```zsh
rasa run actions
```
2. In another command prompt run the following command to run the rasa core server
```zsh
rasa run shell
```

---
> If you have any further queries. Please see the [How-Tos](https://github.com/InCube-camp/newsbot/blob/main/howto.md) section