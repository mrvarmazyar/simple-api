from bottle import default_app, run

import load_app_modules
from snippets import create_tables


create_tables()


run(default_app(), host='0.0.0.0', port=8080)
