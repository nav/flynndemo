
from django.conf.urls import url, include
from allauth.utils import import_attribute
from .provider import KeycloakProvider
from .views import keycloak_admin


def default_urlpatterns(provider):
    login_view = import_attribute(
        provider.get_package() + '.views.oauth2_login')
    callback_view = import_attribute(
        provider.get_package() + '.views.oauth2_callback')


    urlpatterns = [
        url('^login/$',
            login_view, name=provider.id + "_login"),
        url('^login/callback/$',
            callback_view, name=provider.id + "_callback"),
        
        url('^login/callback/(?P<action>[^/]+)$',
            keycloak_admin, name=provider.id + "_admin"),
    ]

    return [url('^' + provider.get_slug() + '/', include(urlpatterns))]

urlpatterns = default_urlpatterns(KeycloakProvider)