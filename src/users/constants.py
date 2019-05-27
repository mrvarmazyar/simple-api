import os

cwd = os.path.join(os.path.dirname(__file__), 'schema')

CREATE_SCHEMA_PATH = os.path.join(cwd, 'create.json')
UPDATE_SCHEMA_PATH = os.path.join(cwd, 'update.json')
