from peewee import PostgresqlDatabase

import configs

connection = PostgresqlDatabase(configs.DB.NAME,
                                host=configs.DB.HOST,
                                user=configs.DB.USER,
                                password=configs.DB.PASSWORD,
                                port=configs.DB.PORT)
