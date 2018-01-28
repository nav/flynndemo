import requests
from django import http
from django.conf import settings
from django.contrib.auth import logout
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
    OAuth2View)

from .provider import OktaProvider


class OktaOAuth2Adapter(OAuth2Adapter):
    provider_id = OktaProvider.id
    access_token_url = settings.OKTA_ACCESS_TOKEN_URL
    authorize_url = settings.OKTA_AUTHORIZE_URL
    profile_url = settings.OKTA_PROFILE_URL

    def complete_login(self, request, app, token, **kwargs):
        resp = requests.post(self.profile_url,
                             data={'access_token': token.token})
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)

class OAuth2LogoutView(OAuth2View):
    def dispatch(self, request):
        logout(request)
        return http.HttpResponseRedirect('/')


oauth2_login = OAuth2LoginView.adapter_view(OktaOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(OktaOAuth2Adapter)
oauth2_logout = OAuth2LogoutView.adapter_view(OktaOAuth2Adapter)
