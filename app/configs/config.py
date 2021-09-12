"""Keeping all global variables here"""
import os
import json
from dataclasses import dataclass


@dataclass
class Config:
    # pylint: disable=too-many-instance-attributes,unused-argument
    """Singleton. Keeps configuration for the application. Reads file if that exists. If not - uses default values"""

    _inited = False

    client_id: str
    client_secret: str
    api_base_url: str
    access_token_url: str
    authorize_url: str

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if not self._inited:
            configs = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config.json')
            if os.path.exists(configs):
                with open(configs, 'r') as config_file:
                    loaded_config = json.load(config_file)
                for env_name, env_value in loaded_config.items():
                    if env_value != '':
                        os.environ[env_name] = str(env_value)

            self.client_id = os.environ.get('CLIENT_ID')
            self.client_secret = os.environ.get('CLIENT_SECRET')
            self.api_base_url = os.environ.get('API_BASE_URL')
            self.access_token_url = os.environ.get('ACCESS_TOKEN_URL')
            self.authorize_url = os.environ.get('AUTHORIZE_URL')

            self._inited = True

    def __repr__(self) -> str:
        return (
            f'client_id: {self.client_id}\n'
            f'client_secret: {self.client_secret}\n'
            f'api_base_url: {self.api_base_url}\n'
            f'access_token_url: {self.access_token_url}\n'
            f'authorize_url: {self.authorize_url}\n'
        )


config = Config()
