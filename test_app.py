#
# StringLocator - 24 hour programming challenge
#
# [test_searchabletext.py]
# Unit tests for REST API (app.py)
#

import unittest, json
from app import app

SEARCH = "/stringlocator/api/v1.0/search/"
LARGE_ID = "121b425579e19849"
SMALL_ID = "7a8764b75df898c1"

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # Return codes

    def test_valid_request(self):
        response = self.app.get(SEARCH + LARGE_ID + "?q=dream")
        self.assertEqual(response.status_code, 200)

    def test_invalid_id(self):
        response = self.app.get(SEARCH + "1234567890abcdef" + "?q=dream")
        self.assertEqual(response.status_code, 404)

    def test_missing_query(self):
        response = self.app.get(SEARCH + LARGE_ID)
        self.assertEqual(response.status_code, 400)

    def test_empty_query(self):
        response = self.app.get(SEARCH + LARGE_ID + "?q=")
        self.assertEqual(response.status_code, 400)

    # Query results

    def test_number_of_occurrences(self):
        response = self.app.get(SEARCH + LARGE_ID + "?q=dream")
        self.assertEqual(json.loads(response.data).get("number_of_occurrences"), 11)

    def test_no_occurrences(self):
        response = self.app.get(SEARCH + LARGE_ID + "?q=pear")
        self.assertEqual(json.loads(response.data).get("number_of_occurrences"), 0)

    def test_query_text(self):
        response = self.app.get(SEARCH + LARGE_ID + "?q=pear")
        self.assertEqual(json.loads(response.data).get("query_text"), "pear")

    # TODO: Write more unit tests!
