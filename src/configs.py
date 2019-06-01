import os


class APP:
    HOST = os.environ.get('APP_HOST', '0.0.0.0')
    PORT = os.environ.get('APP_PORT', 8080)


class DB:
    NAME = os.environ['DB_NAME']
    HOST = os.environ['DB_HOST']
    USER = os.environ['DB_USER']
    PASSWORD = os.environ['DB_PASSWORD']
    PORT = os.environ.get('DB_PORT', 5432)
