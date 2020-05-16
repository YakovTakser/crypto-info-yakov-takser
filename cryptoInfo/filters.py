import django_filters

from .models import Crypto


class CryptoFilter(django_filters.FilterSet):
    class Meta:
        model = Crypto
        fields = ['name', 'author', 'title', 'publishedAt']