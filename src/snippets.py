import json

import jsonschema

import db
from users.models import User


def create_tables():

    # It will be an idempotent action: if there is already a corresponding table,
    #   following would leave it untouched
    db.connection.create_tables([User])


def _load_json(file_path):
    with open(file_path) as f:
        content = json.load(f)
    return content


def validate_data(data, schema_path):
    schema = _load_json(schema_path)

    try:
        jsonschema.validate(data, schema)
    except jsonschema.exceptions.ValidationError as exc:
        return {exc.path[0]: exc.message}
