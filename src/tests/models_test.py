import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import db
from users.models import User


class UserModelTests(unittest.TestCase):

    def setUp(self):
        User.create(username='testUsername', birthday='1990-02-19')

    def tearDown(self):
        db.connection.rollback()
        User.delete().where(User.username == 'testUsername').execute()

    def test_create_username(self):
        user = User.get(username='testUsername')
        self.assertEqual(user.username, 'testUsername')

    def test_create_birthday(self):
        user = User.get(username='testUsername')
        self.assertEqual(user.birthday.strftime('%Y-%m-%d'), '1990-02-19')

    def test_safe(self):
        with self.assertRaises(User.integrity_error):
            User.create(username='testUsername')


if __name__ == '__main__':
    unittest.main()
