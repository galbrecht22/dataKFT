import requests
from requests.exceptions import RequestException
from src.model.tenderDetails import TenderDetailsSchema


class TenderDetailsAPIController:
    def __init__(self):
        self.base_url = 'https://tenders.guru/api/hu'
        self.endpoint = 'tenders'

    def get_endpoint(self, tender_id: int) -> TenderDetailsSchema:
        url = f'{self.base_url}/{self.endpoint}/{tender_id}/source_data'
        try:
            response = requests.get(url=url)
            response.raise_for_status()
            response = TenderDetailsSchema(**response.json())

            return response

        except RequestException as e:
            print(f'Error while connecting to {url}')
            raise e
