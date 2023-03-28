import unittest
import requests
import json

class myTestCase(unittest.TestCase):
    def test_api(self):
        response = requests.get("https://reqres.in/api/users?page=2")
        assert (response.status_code == 200), "Status code not 200 , rather than : " + str(response.status_code)
        for record in response.json()['data']:
            if record['id'] == 7:
                assert record['first_name'] == "Michael"
                "First Name matched"
                assert record['last_name'] == "Lawson"
                "Last Name matched"
