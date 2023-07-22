```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
OAUTH_CLIENT_ID = os.getenv('OAUTH_CLIENT_ID')
OAUTH_CLIENT_SECRET = os.getenv('OAUTH_CLIENT_SECRET')
SSO_SERVICE_URL = os.getenv('SSO_SERVICE_URL')
SAML_ISSUER_URL = os.getenv('SAML_ISSUER_URL')
SAML_IDENTITY_PROVIDER_URL = os.getenv('SAML_IDENTITY_PROVIDER_URL')

# Check if environment variables are set
if not all([OAUTH_CLIENT_ID, OAUTH_CLIENT_SECRET, SSO_SERVICE_URL, SAML_ISSUER_URL, SAML_IDENTITY_PROVIDER_URL]):
    raise EnvironmentError('Required environment variables are not set.')

# Import other modules
from src.authentication_server import AuthenticationServer
from src.application_server import ApplicationServer
from src.client_app import ClientApp

# Initialize servers and app with environment variables
authentication_server = AuthenticationServer(OAUTH_CLIENT_ID, OAUTH_CLIENT_SECRET, SSO_SERVICE_URL, SAML_ISSUER_URL, SAML_IDENTITY_PROVIDER_URL)
application_server = ApplicationServer(OAUTH_CLIENT_ID, OAUTH_CLIENT_SECRET, SSO_SERVICE_URL, SAML_ISSUER_URL, SAML_IDENTITY_PROVIDER_URL)
client_app = ClientApp(OAUTH_CLIENT_ID, OAUTH_CLIENT_SECRET, SSO_SERVICE_URL, SAML_ISSUER_URL, SAML_IDENTITY_PROVIDER_URL)

# Start servers and app
authentication_server.start()
application_server.start()
client_app.start()
```