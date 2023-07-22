```python
import os
from authentication_server import AuthenticationServer
from application_server import ApplicationServer
from client_app import ClientApp
from environment_variables import load_env_vars
from sso import SSO
from oauth import OAuth
from saml import SAML
from security import Security
from scalability import Scalability
from availability import Availability

# Load environment variables
env_vars = load_env_vars()

# Initialize SSO, OAuth, and SAML
sso = SSO(env_vars['SSO_SERVICE_URL'])
oauth = OAuth(env_vars['OAUTH_CLIENT_ID'], env_vars['OAUTH_CLIENT_SECRET'])
saml = SAML(env_vars['SAML_ISSUER_URL'], env_vars['SAML_IDP_URL'])

# Initialize Security, Scalability, and Availability
security = Security()
scalability = Scalability()
availability = Availability()

# Initialize servers and client app
authentication_server = AuthenticationServer(sso, oauth, saml, security)
application_server = ApplicationServer(sso, oauth, saml, scalability, availability)
client_app = ClientApp(authentication_server, application_server)

# Run the client app
if __name__ == "__main__":
    client_app.run()
```