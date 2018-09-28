#
# StringLocator - 24 hour programming challenge
#
# [testsearchabletext.py]
# Unit tests for SearchableText (searchabletext.py)
#

import unittest
from searchabletext import SearchableText
from app import TEXT_PATH


class TestSearchableText(unittest.TestCase):

    def setUp(self):
        self.st = SearchableText(TEXT_PATH)

    def test_id(self):
        """
        Confirm a consistent id is generated from the provided text
        """
        self.assertEqual(self.st.get_id(), '2291bb03208a044b121b425579e19849')

    def test_example_query(self):
        """
        Confirm that the provided example "Now is" returns expected results
        """
        EXAMPLE_QUERY = "Now is"
        EXPECTED = {
            "query_text": "Now is",
            "number_of_occurrences": 3,
            "occurrences": [
                {
                    "line": 45,
                    "start": 17,
                    "end": 23,
                    "in_sentence": "Now is the time to rise from the dark and desolate valley of "
                                   "segregation to the sunlit path of racial justice."
                },
                {
                    "line": 46,
                    "start": 62,
                    "end": 68,
                    "in_sentence": "Now is the time to open the doors of opportunity to all of "
                                   "God's children."
                },
                {
                    "line": 48,
                    "start": 1,
                    "end": 7,
                    "in_sentence": "Now is the time to lift our nation from the quicksands of "
                                   "racial injustice to the solid rock of brotherhood."
                }
            ]
        }
        self.assertDictEqual(self.st.process_query(EXAMPLE_QUERY), EXPECTED)
