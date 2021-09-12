# Python AuthO Bootstrap

## To get everything set up follow steps below^

### 1. Create self-signed certificate as the following:

```bash
openssl req -x509 -nodes -sha256 -days 365 -subj "/C=CA/ST=QC/O=Company, Inc./CN=local.dev" -addext "subjectAltName=DNS:local.dev" -newkey rsa:2048 -keyout ./nginx-selfsigned.key -out ./nginx-selfsigned.crt;
```

After certificates were generated place them to the following directories ./nignx/configs/ssl/certs/nginx-selfsigned.crt and ./nignx/configs/ssl/certs/nginx-selfsigned.key


### 2. Set up the application as it says in the documentation [AuthO](https://auth0.com/docs/quickstart/webapp/python/01-login)

Here are some variables that needs to be set in order to the current application to work:
 - Application Login URI - `https://127.0.0.1:8008/login`
 - Allowed Callback URLs - `https://127.0.0.1:8008/`
 - Allowed Logout URLs   - `https://127.0.0.1:8008/logout`

### 3. Fill the corresponding fields in the config.json
Or you can set up the same values as environment variables in docker-compose.yml

```json
{
  "CLIENT_ID": "client id taken from the AuthO application settings",
  "CLIENT_SECRET": "client secret taken from the AuthO application settings",
  "API_BASE_URL": "https://<your domain taken from the AuthO application settings>",
  "ACCESS_TOKEN_URL": "https://<your domain taken from the AuthO application settings>/oauth/token",
  "AUTHORIZE_URL": "https://<your domain taken from the AuthO application settings>/authorize"
}
```

### 4. Start application up

```bash
    docker-compose up --build
```

Now go to the https://127.0.0.1:8008/ and press Login
