import unittest
from datetime import date
from http import HTTPStatus

import requests

import configs


def _get_full_url(route):
    return 'http://{host}:{port}{route}'.format(host=configs.APP.HOST,
                                                port=configs.APP.PORT,
                                                route=route)


class APITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        requests.delete(_get_full_url('/hello/testUsername'))

    def test_not_found_user(self):
        result = requests.get(_get_full_url('/hello/no_user'))

        self.assertEqual(result.status_code, HTTPStatus.NOT_FOUND)

    def test_invalid_username(self):
        result = requests.post(_get_full_url('/hello'),
                               json={'username': 'user1'})

        self.assertEqual(result.status_code, HTTPStatus.BAD_REQUEST)
        self.assertIn('username', result.json())

    def test_invalid_birthday(self):
        result = requests.post(_get_full_url('/hello'),
                               json={'username': 'testUsername',
                                     'birthday': '199-02-19'})

        self.assertEqual(result.status_code, HTTPStatus.BAD_REQUEST)
        self.assertIn('birthday', result.json())

    def test_create_user(self):
        result = requests.post(_get_full_url('/hello'),
                               json={'username': 'testUsername',
                                     'birthday': '1990-02-19'})

        self.assertEqual(result.status_code, HTTPStatus.CREATED)
        self.assertEqual(result.json()['username'], 'testUsername')

    def test_duplicate_user(self):
        result = requests.post(_get_full_url('/hello'),
                               json={'username': 'testUsername',
                                     'birthday': '1990-02-19'})

        self.assertEqual(result.status_code, HTTPStatus.CONFLICT)

    def test_get_user(self):
        result = requests.get(_get_full_url('/hello/testUsername'))

        self.assertEqual(result.status_code, HTTPStatus.OK)
        self.assertIn('testUsername', result.json()['message'])

    def test_update_not_found_user(self):
        result = requests.put(_get_full_url('/hello/no_user'))

        self.assertEqual(result.status_code, HTTPStatus.NOT_FOUND)

    def test_update_invalid_date_user(self):
        result = requests.put(_get_full_url('/hello/testUsername'),
                              json={'birthday': str(date.today())})

        self.assertEqual(result.status_code, HTTPStatus.BAD_REQUEST)

    def test_update_user(self):
        result = requests.put(_get_full_url('/hello/testUsername'),
                              json={'birthday': '1990-03-19'})

        self.assertEqual(result.status_code, HTTPStatus.NO_CONTENT)


class DeleteAPITest(unittest.TestCase):

    def test_delete_not_found_user(self):
        result = requests.delete(_get_full_url('/hello/no_user'))

        self.assertEqual(result.status_code, HTTPStatus.NOT_FOUND)

    def test_delete_user(self):
        result = requests.delete(_get_full_url('/hello/testUsername'))

        self.assertEqual(result.status_code, HTTPStatus.NO_CONTENT)


if __name__ == '__main__':
    unittest.main()
