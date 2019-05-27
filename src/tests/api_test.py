import unittest
from datetime import date
from http import HTTPStatus

import requests


BASE_URL = 'http://localhost:8080{}'


class APITests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        requests.delete(BASE_URL.format('/hello/testUsername'))

    def test_not_found_user(self):
        result = requests.get(BASE_URL.format('/hello/no_user'))

        self.assertEqual(result.status_code, HTTPStatus.NOT_FOUND)

    def test_invalid_username(self):
        result = requests.post(BASE_URL.format('/hello'),
                               json={'username': 'user1'})

        self.assertEqual(result.status_code, HTTPStatus.BAD_REQUEST)
        self.assertIn('username', result.json())

    def test_invalid_birthday(self):
        result = requests.post(BASE_URL.format('/hello'),
                               json={'username': 'testUsername',
                                     'birthday': '199-02-19'})

        self.assertEqual(result.status_code, HTTPStatus.BAD_REQUEST)
        self.assertIn('birthday', result.json())

    def test_create_user(self):
        result = requests.post(BASE_URL.format('/hello'),
                               json={'username': 'testUsername',
                                     'birthday': '1990-02-19'})

        self.assertEqual(result.status_code, HTTPStatus.CREATED)
        self.assertEqual(result.json()['username'], 'testUsername')

    def test_duplicate_user(self):
        result = requests.post(BASE_URL.format('/hello'),
                               json={'username': 'testUsername',
                                     'birthday': '1990-02-19'})

        self.assertEqual(result.status_code, HTTPStatus.CONFLICT)

    def test_get_user(self):
        result = requests.get(BASE_URL.format('/hello/testUsername'))

        self.assertEqual(result.status_code, HTTPStatus.OK)
        self.assertIn('testUsername', result.json()['message'])

    def test_update_not_found_user(self):
        result = requests.put(BASE_URL.format('/hello/no_user'))

        self.assertEqual(result.status_code, HTTPStatus.NOT_FOUND)

    def test_update_invalid_date_user(self):
        result = requests.put(BASE_URL.format('/hello/testUsername'),
                              json={'birthday': str(date.today())})

        self.assertEqual(result.status_code, HTTPStatus.BAD_REQUEST)

    def test_update_user(self):
        result = requests.put(BASE_URL.format('/hello/testUsername'),
                              json={'birthday': '1990-03-19'})

        self.assertEqual(result.status_code, HTTPStatus.NO_CONTENT)


class DeleteAPITest(unittest.TestCase):

    def test_delete_not_found_user(self):
        result = requests.delete(BASE_URL.format('/hello/no_user'))

        self.assertEqual(result.status_code, HTTPStatus.NOT_FOUND)

    def test_delete_user(self):
        result = requests.delete(BASE_URL.format('/hello/testUsername'))

        self.assertEqual(result.status_code, HTTPStatus.NO_CONTENT)


if __name__ == '__main__':
    unittest.main()
