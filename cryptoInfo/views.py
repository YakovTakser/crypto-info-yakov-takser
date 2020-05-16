from .filters import CryptoFilter
from .forms import SortForm
from .models import Crypto
from django.views.generic import ListView
import requests
import datetime


# Create your views here.

class CryptoArticles(ListView):
    """View Shows all articles of crypto coins"""
    model = Crypto
    template_name = 'cryptoInfo/crypto.html'

    def get(self, request, *args, **kwargs):
        """Get all Articles objects and show them to the user"""
        self.object_list = self.get_queryset()
        sort_form = SortForm
        crypto_filter = CryptoFilter(request.GET, queryset=self.object_list)
        context = self.get_context_data(object_list=self.object_list, form=sort_form, filter=crypto_filter)
        return self.render_to_response(context)

    def get_ordering(self):
        """Sort Articles by chosen field and
         Filter Articles bu chosen fields"""
        ordering = ""
        if self.request.GET.get('sort') != 'None':
            ordering = self.request.GET.get('sort')
            if self.request.GET.get('descending') == 'on':
                ordering = "-" + ordering
            return ordering
        return