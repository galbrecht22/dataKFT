import os
import mysql.connector
from typing import List
from dotenv import load_dotenv


class MySQLController:

    class MySQLConnection:

        def __init__(self, host='localhost', port=3306, db='dataKFT'):
            self.host = host
            self.port = port
            self.db = db
            self.connection = None

            load_dotenv(dotenv_path='config/.env')

            self.username = os.getenv('MYSQL_TENDER_USER')
            self.password = os.getenv('MYSQL_TENDER_PASS')

        def __enter__(self):
            try:
                print('Connecting to MySQL...')
                self.connection = mysql.connector.connect(
                    host=self.host, port=self.port, db=self.db, user=self.username, password=self.password
                )
            except mysql.connector.errors.Error as e:
                print(f'Could not connect to {self.host}:{self.port}. Error: {e}')
                raise e
            else:
                print(f'Connected to {self.host}:{self.port}.')
                return self.connection

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.connection.close()
            print('Connection closed.')

    def __init__(self, database_name: str = 'dataKFT'):
        self.connection = self.MySQLConnection()
        self.database_name = database_name

    def build(self):
        print('Initializing database objects...')

        s = {}
        for i, obj in enumerate(['tender', 'purchaser', 'ship']):
            for layer in ['raw', 'stg', f't0{i+1}']:
                with open(f'../sql/ddl/{layer}_{obj}.sql', 'r') as f:
                    statement = f.read()
                s[f'{layer}_{obj}'] = statement

        with self.connection as connection:
            for obj, stmt in s.items():
                print(f'Executing DDL statement for `{obj}` object...')
                # print(f'Statement:\n{stmt}')
                with connection.cursor() as cursor:
                    cursor.execute(stmt)
                    for statement, result_set in cursor.fetchsets():
                        pass
                    connection.commit()
                print(f'Statement executed successfully for `{obj}` object.')
        print('Environment initialized successfully.')

    def bulk_insert(self, obj_name: str, values: List[tuple]):
        sql = f"INSERT INTO {obj_name} VALUES ({', '.join(['%s' for _ in range(len(values[0]))])})"
        with self.connection as connection:
            print(f'Executing INSERT statement for `{obj_name}` object...')
            # print(f'Statement:\n{sql}')
            with connection.cursor() as cursor:
                cursor.executemany(sql, values)
                print(f'{cursor.rowcount} rows inserted.')
                for statement, result_set in cursor.fetchsets():
                    pass
                connection.commit()
            print(f'Statement executed successfully for `{obj_name}` object.')

    def populate(self, object_names: List[str]):
        statements = {}
        for object_name in object_names:
            with open(f'../sql/dml/{object_name}.sql', 'r') as f:
                statements[object_name] = f.read()
        with self.connection as connection:
            with connection.cursor() as cursor:
                for object_name, statement in statements.items():
                    print(f'Executing INSERT statement for `{object_name}` object...')
                    cursor.execute(statement)
                    # print(f'{cursor.rowcount} rows inserted into {object_name}.')
                    for stmt, result_set in cursor.fetchsets():
                        pass
                    print(f'INSERT statement executed successfully.')

                connection.commit()
                print(f'Statements executed successfully for objects: `{object_names}`.')
