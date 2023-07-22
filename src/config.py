```python
import os

class Config:
    def __init__(self):
        self.OAUTH_CLIENT_ID = os.getenv('OAUTH_CLIENT_ID')
        self.OAUTH_CLIENT_SECRET = os.getenv('OAUTH_CLIENT_SECRET')
        self.SSO_SERVICE_URL = os.getenv('SSO_SERVICE_URL')
        self.SAML_ISSUER_URL = os.getenv('SAML_ISSUER_URL')
        self.SAML_IDENTITY_PROVIDER_URL = os.getenv('SAML_IDENTITY_PROVIDER_URL')

    def validate(self):
        if not all([self.OAUTH_CLIENT_ID, self.OAUTH_CLIENT_SECRET, self.SSO_SERVICE_URL, self.SAML_ISSUER_URL, self.SAML_IDENTITY_PROVIDER_URL]):
            raise ValueError("Missing required environment variable")

config = Config()
config.validate()
```