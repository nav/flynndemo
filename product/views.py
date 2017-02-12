from django import http
from django.views.generic.base import TemplateView, View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = "base.html"

class ProfileView(TemplateView):
    template_name = "profile.html"

class ProductListView(LoginRequiredMixin, TemplateView):
    template_name = "product_list.html"

