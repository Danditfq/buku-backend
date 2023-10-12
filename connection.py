import psycopg2
from google.cloud import secretmanager
import json

class Connection:
    def __init__(self):
        # Retrieve the secrets from Google Secret Manager
        secret_name = "projects/866025455973/secrets/connection-db/versions/latest"
        secret_payload = get_secrets(secret_name)
        credentials = json.loads(secret_payload)

        # Establish the database connection
        self.conn = psycopg2.connect(
            database=credentials["database"],
            host=credentials["host"],
            user=credentials["user"],
            password=credentials["password"],
            port=credentials["port"]
        )

    def getConnection(self):
        return self.conn

def get_secrets(secret_name):
    client = secretmanager.SecretManagerServiceClient()
    secret_version = client.access_secret_version(name=secret_name)
    secret_payload = secret_version.payload.data.decode("UTF-8")
    return secret_payload