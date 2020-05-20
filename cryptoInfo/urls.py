from django.urls import path
from django.views.decorators.cache import cache_page
from .views import CryptoArticles

urlpatterns = [
    path('', cache_page(60 * 1)(CryptoArticles.as_view()), name='crypto_articles'),
]
