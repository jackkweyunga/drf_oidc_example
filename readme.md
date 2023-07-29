# DJANGO MICRO SERVICE 

An example for a django microservice project.

## Features

- [x] Authentication and Authorization API using mozilla-dajngo-oidc package
- [x] Keycloak Compatible

## Endpoints:

| Endpoints  | Description                                                                                                               |
|------------|---------------------------------------------------------------------------------------------------------------------------|
| /          | A public api endpoint                                                                                                     |
| /protected | A protected endpoint; requires an authenticated user. Requires an Bearer token passed in the request Authorization header |

## Setup

create a `.env` file and add the following with there values:

```dotenv

OIDC_RP_CLIENT_ID=
OIDC_RP_CLIENT_SECRET=
OIDC_OP_AUTHORIZATION_ENDPOINT=
OIDC_OP_TOKEN_ENDPOINT=
OIDC_OP_USER_ENDPOINT=
OIDC_OP_END_SESSION_ENDPOINT=
OIDC_OP_JWKS_ENDPOINT=

```

