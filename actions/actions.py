# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from datetime import datetime
from .config import news_api as news


class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        now = datetime.now()

        if now.hour < 12:
            day = 'Morning'
        elif now.hour < 18:
            day = 'Afternoon'
        else:
            day = 'Evening'

        dispatcher.utter_message(text=f"Hello! Good {day}")

        return []


class ActionHeadlines(Action):

    def name(self) -> Text:
        return 'action_headlines'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        news_items = news.get_top_headlines()
        if news_items.get('totalResults', 0) > 0:
            articles = news_items['articles']
            for article in articles[:3]:
                title = article['title']
                description = article['description']
                url = article['url']
                image_url = article['urlToImage']
                source = article['source']['name']

                message = f'{title}\n[see more]({url})'
                dispatcher.utter_message(text=message, image=image_url)
        else:
            dispatcher.utter_message(text='No recent news on the topic.')

        return []


class ActionSpecificNews(Action):

    def name(self) -> Text:
        return 'action_specific_news'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        q = (tracker.latest_message['entities'] or [{}])[0].get('value')
        news_items = news.get_everything(q=q, sort_by='relevancy')
        if news_items.get('totalResults', 0) > 0:
            if q:
              dispatcher.utter_message(text=f'Here are some news about *{q}*')
            article = news_items['articles'][0]

            title = article['title']
            description = article['description']
            url = article['url']
            image_url = article['urlToImage']
            source = article['source']['name']

            message = f'{title}\n[see more]({url})'
            dispatcher.utter_message(image=image_url, text=message)
        else:
            dispatcher.utter_message(text=f'No recent news on the topic *{q or ""}*.')

        return []
