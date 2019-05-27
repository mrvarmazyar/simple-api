from bottle import default_app, run

from snippets import create_tables

# loading the whole module through its `routes.py`
from users import routes


create_tables()


run(default_app(), host='0.0.0.0', port=8080)
