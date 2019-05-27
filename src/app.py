from bottle import default_app, run

from snippets import create_tables

# loading the whole module through its `routes.py`
from users import routes


create_tables()


run(default_app(), port=8080)
