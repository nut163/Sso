```python
import os
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

# Environment Variables
OAUTH_CLIENT_ID = os.getenv("OAUTH_CLIENT_ID")
OAUTH_CLIENT_SECRET = os.getenv("OAUTH_CLIENT_SECRET")

class OAuth:
    def __init__(self):
        self.client_id = OAUTH_CLIENT_ID
        self.client_secret = OAUTH_CLIENT_SECRET
        self.client = BackendApplicationClient(client_id=self.client_id)
        self.oauth = OAuth2Session(client=self.client)

    def get_token(self, token_url):
        return self.oauth.fetch_token(token_url=token_url, client_id=self.client_id, client_secret=self.client_secret)

    def request(self, method, url, **kwargs):
        return self.oauth.request(method, url, **kwargs)
```