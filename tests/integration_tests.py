import unittest
from src import main, authentication_server, application_server, client_app
from src import sso, oauth, saml

class IntegrationTests(unittest.TestCase):

    def setUp(self):
        self.main = main.Main()
        self.auth_server = authentication_server.AuthenticationServer()
        self.app_server = application_server.ApplicationServer()
        self.client_app = client_app.ClientApp()
        self.sso = sso.SSO()
        self.oauth = oauth.OAuth()
        self.saml = saml.SAML()

    def test_sso_integration(self):
        response = self.main.handle_request(self.sso)
        self.assertEqual(response.status_code, 200)

    def test_oauth_integration(self):
        response = self.main.handle_request(self.oauth)
        self.assertEqual(response.status_code, 200)

    def test_saml_integration(self):
        response = self.main.handle_request(self.saml)
        self.assertEqual(response.status_code, 200)

    def test_auth_server_integration(self):
        response = self.main.handle_request(self.auth_server)
        self.assertEqual(response.status_code, 200)

    def test_app_server_integration(self):
        response = self.main.handle_request(self.app_server)
        self.assertEqual(response.status_code, 200)

    def test_client_app_integration(self):
        response = self.main.handle_request(self.client_app)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()