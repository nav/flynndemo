from django import http
from django.views.generic.base import TemplateView, View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .tasks import change_prices
from .models import Product

class HomePageView(TemplateView):
    template_name = "base.html"

class ProfileView(TemplateView):
    template_name = "profile.html"

class ProductListView(LoginRequiredMixin, TemplateView):
    template_name = "product_list.html"

    def get_context_data(self, *args, **kwargs):
    	context = super().get_context_data(*args, **kwargs)
    	context['products'] = Product.objects.all()
    	change_prices.delay()
    	return context

