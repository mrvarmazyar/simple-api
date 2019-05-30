import os


class APP:
    HOST = os.environ.get('APP_HOST', '0.0.0.0')
    PORT = os.environ.get('APP_PORT', 8080)
