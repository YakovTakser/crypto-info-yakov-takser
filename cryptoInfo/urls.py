from django.urls import path

from .views import CryptoArticles

urlpatterns = [
    path('', CryptoArticles.as_view(), name='crypto_articles'),
]
