```python
import os
from flask import Flask, request, redirect, url_for
from src.sso import SSO
from src.oauth import OAuth
from src.saml import SAML
from src.security import Security
from src.scalability import Scalability
from src.availability import Availability

app = Flask(__name__)

# Initialize with environment variables
sso_service = SSO(os.getenv('SSO_SERVICE_URL'))
oauth_service = OAuth(os.getenv('OAUTH_CLIENT_ID'), os.getenv('OAUTH_CLIENT_SECRET'))
saml_service = SAML(os.getenv('SAML_ISSUER_URL'), os.getenv('SAML_IDP_URL'))
security_service = Security()
scalability_service = Scalability()
availability_service = Availability()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user
        user = request.form['username']
        password = request.form['password']
        if sso_service.authenticate(user, password) or oauth_service.authenticate(user, password):
            return redirect(url_for('home'))
        else:
            return 'Invalid credentials', 401
    return 'Login Page'

@app.route('/home', methods=['GET'])
def home():
    # Check system availability
    if not availability_service.is_available():
        return 'Service is currently unavailable', 503
    return 'Home Page'

if __name__ == '__main__':
    # Ensure high security and scalability
    security_service.enforce_security(app)
    scalability_service.enforce_scalability(app)
    app.run(host='0.0.0.0', port=5000)
```