# Setup Guide

This guide will walk you through the setup process for our Single Sign-On (SSO) and OAuth solution.

## Prerequisites

Ensure you have Python installed on your system. If not, you can download it from [here](https://www.python.org/downloads/).

## Clone the Repository

First, clone the repository to your local machine using the following command:

```
git clone <repository_url>
```

## Install Dependencies

Navigate to the project directory and install the required dependencies using the following command:

```
pip install -r requirements.txt
```

## Environment Variables

You need to set up the following environment variables:

- `OAUTH_CLIENT_ID`: Your OAuth client ID.
- `OAUTH_CLIENT_SECRET`: Your OAuth client secret.
- `SSO_SERVICE_URL`: The URL of your SSO service.
- `SAML_ISSUER_URL`: The URL of your SAML issuer.
- `SAML_IDENTITY_PROVIDER_URL`: The URL of your SAML identity provider.

You can set these variables in the `src/environment_variables.py` file.

## Run the Application

You can run the application using the following command:

```
python src/main.py
```

## Testing

To run the unit, integration, and security tests, use the following commands:

```
python -m unittest tests/unit_tests.py
python -m unittest tests/integration_tests.py
python -m unittest tests/security_tests.py
```

## Documentation

For more information on how to use the application, refer to the `docs/user_guide.md` and `docs/developer_guide.md` files.

## Milestones

To understand the development process and future improvements, refer to the `docs/milestones.md` file.