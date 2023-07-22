# User Guide

## Getting Started

To get started with our Single Sign-On (SSO) and OAuth solution, you will need to set up the environment variables and configure the system.

### Environment Variables

Set the following environment variables:

- `OAUTH_CLIENT_ID`: Your OAuth client ID.
- `OAUTH_CLIENT_SECRET`: Your OAuth client secret.
- `SSO_SERVICE_URL`: The URL of your SSO service.
- `SAML_ISSUER_URL`: The URL of your SAML issuer.
- `SAML_IDENTITY_PROVIDER_URL`: The URL of your SAML identity provider.

You can set these variables in the `src/environment_variables.py` file.

### System Configuration

Configure the system by running the `src/setup.py` script. This will set up the Authentication Server, Application Server, and Client App.

## Using the System

Once the system is set up, you can start using the SSO and OAuth functionalities.

### Single Sign-On (SSO)

To use the SSO functionality, navigate to the `src/sso.py` file and call the SSO function.

### OAuth 2.0

To use the OAuth 2.0 functionality, navigate to the `src/oauth.py` file and call the OAuth function.

### SAML 2.0 Integration

To use the SAML 2.0 integration, navigate to the `src/saml.py` file and call the SAML function.

## Security, Scalability, and Availability

Our system ensures high security, scalability, and availability. You can check these aspects in the `src/security.py`, `src/scalability.py`, and `src/availability.py` files respectively.

## Testing

We have implemented Unit, Integration, and Security Testing. You can run these tests from the `tests/` directory.

## Further Documentation

For more detailed information, refer to the `docs/developer_guide.md` and `docs/setup_guide.md` files. For information about the project milestones, refer to the `docs/milestones.md` file.