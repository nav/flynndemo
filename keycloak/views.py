import requests
from django import http
from django.conf import settings
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt 
from django.utils.decorators import method_decorator

from allauth.socialaccount.models import SocialToken, SocialAccount
from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter,
                                                          OAuth2LoginView,
                                                          OAuth2CallbackView)

from .provider import KeycloakProvider


class KeycloakOAuth2Adapter(OAuth2Adapter):
    provider_id = KeycloakProvider.id
    access_token_url = settings.KEYCLOAK_ACCESS_TOKEN_URL
    authorize_url = settings.KEYCLOAK_AUTHORIZE_URL
    profile_url = settings.KEYCLOAK_PROFILE_URL

    def complete_login(self, request, app, token, **kwargs):
        resp = requests.post(self.profile_url,
                             data={'access_token': token.token})
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)


class KeycloakAdminView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(KeycloakAdminView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
      handler = getattr(self, kwargs.get('action'), None)
      if handler is not None:
        return handler(request, *args, **kwargs)
      return http.HttpResponse('Handler not found')

    def k_push_not_before(self, request, *args, **kwargs):
      header, body, signature = request.body.split('.')
      account_ids = SocialToken.objects.filter(token__istartswith=header)\
                                       .values_list('account_id', flat=True)
      user_ids = SocialAccount.objects.filter(pk__in=account_ids)\
                                      .values_list('user_id', flat=True)
      users = User.objects.filter(pk__in=user_ids)
      for user in users:
        [s.delete() for s in Session.objects.all() if s.get_decoded().get('_auth_user_id') == str(user.pk)]
      
      return http.HttpResponse('ok')

    def decode_base64(data):
      # http://stackoverflow.com/a/9807138
      missing_padding = len(data) % 4
      if missing_padding != 0:
          data += b'='* (4 - missing_padding)
      return base64.decodestring(data)


oauth2_login = OAuth2LoginView.adapter_view(KeycloakOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(KeycloakOAuth2Adapter)
keycloak_admin = KeycloakAdminView.as_view()
