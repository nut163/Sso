```python
import requests
from src import sso, oauth, saml
from src import environment_variables as env

class ClientApp:
    def __init__(self):
        self.oauth_client_id = env.OAuth_Client_ID
        self.oauth_client_secret = env.OAuth_Client_Secret
        self.sso_service_url = env.SSO_Service_URL
        self.saml_issuer_url = env.SAML_Issuer_URL
        self.saml_identity_provider_url = env.SAML_Identity_Provider_URL

    def authenticate(self, username, password):
        # SSO Authentication
        sso_auth = sso.authenticate(username, password, self.sso_service_url)
        if not sso_auth:
            return "SSO Authentication Failed"

        # OAuth 2.0 Authentication
        oauth_auth = oauth.authenticate(self.oauth_client_id, self.oauth_client_secret)
        if not oauth_auth:
            return "OAuth Authentication Failed"

        # SAML 2.0 Integration
        saml_auth = saml.integrate(self.saml_issuer_url, self.saml_identity_provider_url)
        if not saml_auth:
            return "SAML Integration Failed"

        return "Authentication Successful"

if __name__ == "__main__":
    client_app = ClientApp()
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    print(client_app.authenticate(username, password))
```