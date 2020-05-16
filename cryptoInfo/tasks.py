import datetime
import requests
from celery import shared_task
from .models import Crypto

@shared_task
def getCryptoInfo():
    """Get articles of crypto coins and store them to the database"""

    # Take data about crypto coins from an api
    today_date = datetime.date.today()
    response = requests.get(f'http://newsapi.org/v2/everything?q=bitcoin&from={today_date}&sortBy=publishedAt&apiKey=8033b988fade40de9105a3cf6f4547a3')
    cryptoData = response.json()

    # Calculate how many of new articles exist
    num_of_articles_created_today = Crypto.objects.filter(publishedAt__date=today_date).count()
    num_of_new_articles = len(cryptoData['articles']) - num_of_articles_created_today

    # Testing purpose of Calculate how many of new articles exist
    # print(today_date)
    # print(f'num of new articles: {num_of_new_articles}')
    # print(f'num of articles created today: {num_of_articles_created_today}')

    # Take new articles and save them to the database
    for article in cryptoData['articles'][:num_of_new_articles]:
        # Take date & time and convert to dateTime field
        date_of_object = article['publishedAt']
        d1 = datetime.datetime.strptime(date_of_object, "%Y-%m-%dT%H:%M:%SZ")
        # Create an article object and store it to the database
        article_obj = Crypto.objects.create(name=article['source']['name'],
                                            author=article['author'],
                                            title=article['title'],
                                            description=article['description'],
                                            url=article['url'],
                                            urlToImage=article['urlToImage'],
                                            publishedAt=d1,
                                            content=article['content'])
        article_obj.save()
