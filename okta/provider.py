from allauth.socialaccount import providers
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider



class OktaProvider(OAuth2Provider):
    id = 'okta'
    name = 'Okta'

    def extract_uid(self, data):
        return data['sub']

    def extract_common_fields(self, data):
        return dict(username=data.get('preferred_username'),
                    first_name=data.get('given_name'),
                    last_name=data.get('family_name'),
                    email=data.get('email'))


providers.registry.register(OktaProvider)