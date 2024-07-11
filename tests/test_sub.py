import unittest
from app import app


class TestSubtractEndpoint(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_successful_request(self):
        payload = {'num1': 10, 'num2': 20}
        response = self.app.post('/subtract', json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['result'], -10)

    def test_no_payload(self):
        response = self.app.post('/subtract')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['error'], 'Content-Type must be application/json')

    def test_bad_payload(self):
        payload = {'num1': 'hello', 'num2': 'world'}
        response = self.app.post('/subtract', json=payload)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['error'], 'Bad data, values must be int or float')

