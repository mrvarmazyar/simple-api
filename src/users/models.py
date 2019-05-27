from datetime import date

from peewee import Model, CharField, DateField, DoesNotExist, IntegrityError

from db import db_connection


class BaseModel(Model):
    class Meta:
        database = db_connection

    does_not_exists = DoesNotExist
    integrity_error = IntegrityError


class User(BaseModel):
    username = CharField(unique=True)
    birthday = DateField()

    @property
    def birthday_is_today(self):
        return self.birth_date_diff_in_days == 0

    @property
    def birth_date_diff_in_days(self):
        today = date.today()
        next_birthday = self.birthday.replace(year=today.year)

        if (today.month == next_birthday.month and today.day > next_birthday.day) or \
                today.month > next_birthday.month:
            next_birthday = next_birthday.replace(year=next_birthday.year + 1)

        return (next_birthday - today).days

    def serialize(self):
        return {'id': self.id, 'username': self.username, 'birthday': self.birthday}
