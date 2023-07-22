# Developer Guide

## Getting Started

To get started with the development, clone the repository and install the required dependencies.

## System Architecture

The system comprises of an Authentication Server, Application Server, and Client App. The code for these can be found in `src/authentication_server.py`, `src/application_server.py`, and `src/client_app.py` respectively.

## Authentication

The application supports Single Sign-On (SSO), OAuth 2.0, and SAML 2.0 protocols. The implementation of these can be found in `src/sso.py`, `src/oauth.py`, and `src/saml.py` respectively.

## Environment Variables

The application accepts environment variables during setup. The configuration for these can be found in `src/config.py` and `src/environment_variables.py`.

The following environment variables are required:

- OAuth Client ID/Secret
- SSO Service URL
- SAML Issuer/Identity Provider URL

## Security, Scalability, and Availability

The application ensures high security, provides scalability, and offers high availability. The implementation of these can be found in `src/security.py`, `src/scalability.py`, and `src/availability.py` respectively.

## Testing

The application includes Unit, Integration, and Security Testing. The test cases can be found in `tests/unit_tests.py`, `tests/integration_tests.py`, and `tests/security_tests.py`.

## Documentation

For setup instructions, refer to `docs/setup_guide.md`. For user instructions, refer to `docs/user_guide.md`.

## Milestones

The project is broken down into manageable milestones. The details of these milestones can be found in `docs/milestones.md`.

## Contributing

To contribute to the project, create a branch and submit a pull request. The pull request will be reviewed and merged if it meets the project requirements.