from peewee import SqliteDatabase


db_connection = SqliteDatabase('app.db')

db_connection.connect()
