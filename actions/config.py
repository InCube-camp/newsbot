import os
from newsapi import NewsApiClient

env_key = 'NEWSAPI_KEY'
__api_key = os.getenv(env_key)
news_api = NewsApiClient(api_key=__api_key)

