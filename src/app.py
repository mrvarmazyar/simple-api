from bottle import default_app, run

import configs
import load_app_modules
from snippets import create_tables


create_tables()


run(default_app(), host=configs.APP.HOST, port=configs.APP.PORT)
