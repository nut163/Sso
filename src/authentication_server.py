```python
import os
from sso import SSO
from oauth import OAuth
from saml import SAML

class AuthenticationServer:
    def __init__(self):
        self.sso_service_url = os.getenv('SSO_SERVICE_URL')
        self.oauth_client_id = os.getenv('OAUTH_CLIENT_ID')
        self.oauth_client_secret = os.getenv('OAUTH_CLIENT_SECRET')
        self.saml_issuer_url = os.getenv('SAML_ISSUER_URL')
        self.saml_identity_provider_url = os.getenv('SAML_IDENTITY_PROVIDER_URL')

        self.sso = SSO(self.sso_service_url)
        self.oauth = OAuth(self.oauth_client_id, self.oauth_client_secret)
        self.saml = SAML(self.saml_issuer_url, self.saml_identity_provider_url)

    def authenticate(self, auth_type, credentials):
        if auth_type == 'sso':
            return self.sso.authenticate(credentials)
        elif auth_type == 'oauth':
            return self.oauth.authenticate(credentials)
        elif auth_type == 'saml':
            return self.saml.authenticate(credentials)
        else:
            raise ValueError(f'Invalid authentication type: {auth_type}')

    def is_authenticated(self, auth_type, token):
        if auth_type == 'sso':
            return self.sso.is_authenticated(token)
        elif auth_type == 'oauth':
            return self.oauth.is_authenticated(token)
        elif auth_type == 'saml':
            return self.saml.is_authenticated(token)
        else:
            raise ValueError(f'Invalid authentication type: {auth_type}')
```