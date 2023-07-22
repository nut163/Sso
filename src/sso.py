```python
import requests
from src.environment_variables import SSO_SERVICE_URL

def sso_login(user_credentials):
    """
    Function to authenticate user using Single Sign-On (SSO)
    """
    try:
        response = requests.post(SSO_SERVICE_URL, data=user_credentials)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

    return response.json()

def sso_logout(user_token):
    """
    Function to logout user from Single Sign-On (SSO)
    """
    try:
        response = requests.post(f"{SSO_SERVICE_URL}/logout", data={'token': user_token})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return False
    except Exception as err:
        print(f"An error occurred: {err}")
        return False

    return True
```