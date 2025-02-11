import requests
from requests.exceptions import RequestException
from time import sleep
from dataclasses import asdict
from typing import List
from model.tenderList import ApiResponse, ApiParameters, TenderSchema


class TenderListAPIController:
    def __init__(self):
        self.base_url = 'https://tenders.guru/api/hu'
        self.endpoint = 'tenders'

    def get_endpoint(self, params: ApiParameters) -> ApiResponse:
        url = f'{self.base_url}/{self.endpoint}'
        try:
            response = requests.get(url=url, params=asdict(params))
            response.raise_for_status()
            response = ApiResponse(**response.json())

            return response

        except RequestException as e:
            print(f'Error while connecting to '
                  f'{self.base_url}/{self.endpoint}?{"&".join([f'{k}={v}' for k, v in asdict(params).items()])}')
            raise e

    def get_all_paginated_results(self, pages: int, params: ApiParameters) -> List[TenderSchema]:
        results = []
        start, end = 1, pages  # prod
        # start, end = 2,5       # test
        for page in range(start, end + 1):
            params.page = page
            print(f'Tenders API - Calling page {page}...')
            try:
                response = self.get_endpoint(params)
                results.extend(response.data)
                sleep(0.5)
            except RequestException as e:
                print(f'Error: {e}')
                print('Paginated API calls were interrupted, continuing...')
                break
        return results
