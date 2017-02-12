from django.conf.urls import url
from .views import HomePageView, ProductListView, ProfileView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name="homepage"),
    url(r'^accounts/profile/', ProfileView.as_view(), name="profile"),
    url(r'^products/', ProductListView.as_view(), name="products"),
]
