from src.api.shipsAPI import ShipListAPIController
from src.api.tenderListAPI import TenderListAPIController
from src.api.tenderDetailsAPI import TenderDetailsAPIController
from src.database.mongoConnection import MongoDBController
from src.database.mysqlConnection import MySQLController
from src.model import tenderList
import pandas as pd
from datetime import datetime


class Controller:
    def __init__(self):
        self.tender_list_api_controller = TenderListAPIController()
        self.tender_details_api_controller = TenderDetailsAPIController()
        self.ship_list_api_controller = ShipListAPIController()
        self.mongo_controller = MongoDBController()
        self.mysql_controller = MySQLController()

    def init_environment(self, ingest=False):
        """
        Cleans up and initializes data objects for MongoDB and MySQL databases.

        :parameter:
         ingest: Boolean - whether to initialize MongoDB collection(s) for extract.
        """
        if ingest:
            self.mongo_controller.build()
        self.mysql_controller.build()

    def extract_tender_list(self, date_filter: str = None):
        """
        Executes E2E process of fetching Tender objects from the respective endpoint and store them in MongoDB.

        :parameter:
         date_filter: str - date filter for retrieved list of Tender objects.
                   Applied on object.awarded.{item}.date column.

        :return:
        Count of inserted documents.
        """
        params = tenderList.ApiParameters()
        response = self.tender_list_api_controller.get_endpoint(params)
        results = self.tender_list_api_controller.get_all_paginated_results(response.page_count, params)
        print(f'Total records fetched: {len(results)}')
        results_json = [item.__dict__ for item in results]

        current_ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for item in results_json:
            item['inserted_ts'] = current_ts

        tenders = results_json

        if date_filter:
            results_json_filtered = []
            for obj in results_json:
                for i in range(len(obj['awarded'])):
                    if obj['awarded'][i]['date'] == date_filter:
                        results_json_filtered.append(obj)
                        break
            tenders = results_json_filtered

        return self.mongo_controller.store('tender', tenders)

    def extract_purchasers(self):
        """
        Executes E2E process of extracting Purchaser objects from TenderDetails retrieved from the respective endpoint
        and store them in MongoDB.

        :return:
        Count of inserted documents.
        """

        tenders = self.mongo_controller.load('tender')
        tender_details = [self.tender_details_api_controller.get_endpoint(tender['id']) for tender in tenders]
        print(f'Total records fetched: {len(tender_details)}')

        purchasers = [item.purchaser.__dict__ for item in tender_details]

        current_ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for item in purchasers:
            item['inserted_ts'] = current_ts

        return self.mongo_controller.store('purchaser', purchasers)

    def extract_ships(self):
        """
        Executes E2E process of fetching Ships retrieved from the respective endpoint
        and store them in MongoDB.

        :return:
        Count of inserted documents.
        """
        self.ship_list_api_controller.authorize()
        results = self.ship_list_api_controller.get_endpoint('ships')
        ships = [item.__dict__ for item in results]

        current_ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for item in ships:
            item['inserted_ts'] = current_ts

        return self.mongo_controller.store('ship', ships)

    def load_tenders(self):
        """
        Loads Tender objects from MongoDB, normalizes json structure to fit into relational dataset,
        keeps necessary columns and loads them into MySQL.

        :return:
        Count of inserted rows.
        """
        tenders = self.mongo_controller.load('tender')

        df = pd.json_normalize(tenders, max_level=1)
        df = df[[
            'id',
            'date',
            'title',
            'category',
            'sid',
            'eid',
            'place',
            'purchaser.sid',
            'awarded_value',
            'awarded_currency',
            'awarded_value_eur',
            'inserted_ts'
        ]]

        val = [tuple(x) for x in df.values.tolist()]

        return self.mysql_controller.bulk_insert('raw_tender', val)

    def load_purchasers(self):
        """
        Loads Purchaser objects from MongoDB, normalizes json structure to fit into relational dataset,
        keeps necessary columns and loads them into MySQL.

        :return:
        Count of inserted rows.
        """
        purchasers = self.mongo_controller.load('purchaser')

        df = pd.json_normalize(purchasers, max_level=1)
        df = df[['id',
                 'rovidMegnevezes',
                 'teljesMegnevezes',
                 'szekhely.orszag',
                 'szekhely.iranyitoszam',
                 'szekhely.telepules',
                 'szekhely.kozterNeve',
                 'szekhely.kozterJellege',
                 'szekhely.hazszam',
                 'szekhely.helyrajziszam',
                 'szekhely.nutsKod',
                 'inserted_ts'
                 ]]

        val = [tuple(x) for x in df.values.tolist()]

        return self.mysql_controller.bulk_insert('raw_purchaser', val)

    def load_ships(self):
        """
        Loads Ship objects from MongoDB and loads them into MySQL.

        :return:
        Count of inserted rows.
        """
        ships = self.mongo_controller.load('ship')

        df = pd.DataFrame(ships)

        val = [tuple(x) for x in df.values.tolist()]

        return self.mysql_controller.bulk_insert('raw_ship', val)

    def transform(self):
        """
        Executes predefined transformation logic on data objects.
        """
        self.mysql_controller.populate(['stg_tender', 'stg_purchaser', 'stg_ship'])
        self.mysql_controller.populate(['t01_tender', 't02_purchaser', 't03_ship'])
