import unittest
from src import security, sso, oauth, saml

class TestSecurity(unittest.TestCase):

    def setUp(self):
        self.security = security.Security()
        self.sso = sso.SSO()
        self.oauth = oauth.OAuth()
        self.saml = saml.SAML()

    def test_security_sso(self):
        result = self.security.check_sso_security(self.sso)
        self.assertTrue(result, "SSO security check failed")

    def test_security_oauth(self):
        result = self.security.check_oauth_security(self.oauth)
        self.assertTrue(result, "OAuth security check failed")

    def test_security_saml(self):
        result = self.security.check_saml_security(self.saml)
        self.assertTrue(result, "SAML security check failed")

if __name__ == '__main__':
    unittest.main()