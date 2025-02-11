import os
import requests
from requests.exceptions import RequestException
from typing import List
from model.ships import ShipSchema
from dotenv import load_dotenv


class ShipListAPIController:
    def __init__(self):
        self.base_url = 'https://data-engineer-interview-api.up.railway.app'
        self.bearer_token = None

        load_dotenv(dotenv_path='config/.env')

        self.username = os.getenv('SHIP_API_USER')
        self.password = os.getenv('SHIP_API_PASS')

    def authorize(self):
        url = f'{self.base_url}/auth/login'
        params = {'username': self.username, 'password': self.password}

        try:
            print('Fetching token...')
            response = requests.post(url=url, params=params)
            response.raise_for_status()
            self.bearer_token = response.text
            print('Token fetched successfully.')

        except RequestException as e:
            print(f'Error while connecting to {url}')
            raise e

    def get_endpoint(self, endpoint: str = 'ships') -> List[ShipSchema]:
        url = f'{self.base_url}/{endpoint}'
        headers = {'Authorization': f'Bearer {self.bearer_token}'}

        try:
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()
            response = [ShipSchema(**x) for x in response.json()]

            return response

        except RequestException as e:
            print(f'Error while connecting to {url}')
            raise e

