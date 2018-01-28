from django.conf.urls import url, include
from allauth.utils import import_attribute
from .provider import OktaProvider


def default_urlpatterns(provider):
    login_view = import_attribute(
        provider.get_package() + '.views.oauth2_login')
    logout_view = import_attribute(
        provider.get_package() + '.views.oauth2_logout')
    callback_view = import_attribute(
        provider.get_package() + '.views.oauth2_callback')

    urlpatterns = [
        url('^login/$',
            login_view, name=provider.id + "_login"),
        url('^logout/$',
            logout_view, name=provider.id + "_logout"),
        url('^login/callback/$',
            callback_view, name=provider.id + "_callback"),
    ]

    return [url('^' + provider.get_slug() + '/', include(urlpatterns))]


urlpatterns = default_urlpatterns(OktaProvider)
