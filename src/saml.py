```python
import requests
from xml.etree import ElementTree as ET
from environment_variables import SAML_ISSUER, IDENTITY_PROVIDER_URL

class SAML:
    def __init__(self):
        self.saml_issuer = SAML_ISSUER
        self.identity_provider_url = IDENTITY_PROVIDER_URL

    def create_saml_request(self, user_id):
        saml_request = f"""
        <samlp:AuthnRequest xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
                            ID="{user_id}"
                            Version="2.0"
                            IssueInstant="{self.get_issue_instant()}"
                            ProtocolBinding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
                            ProviderName="SSOProvider"
                            AssertionConsumerServiceURL="{self.saml_issuer}"
                            >
            <saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">{self.saml_issuer}</saml:Issuer>
        </samlp:AuthnRequest>
        """
        return saml_request

    def send_saml_request(self, saml_request):
        headers = {'Content-Type': 'application/xml'}
        response = requests.post(self.identity_provider_url, data=saml_request, headers=headers)
        return response

    def parse_saml_response(self, saml_response):
        tree = ET.ElementTree(ET.fromstring(saml_response.content))
        assertion = tree.find('.//{urn:oasis:names:tc:SAML:2.0:assertion}Assertion')
        return assertion

    def get_issue_instant(self):
        from datetime import datetime
        return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
```