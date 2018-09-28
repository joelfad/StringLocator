#
# StringLocator - 24 hour programming challenge
#
# [testsearchabletext.py]
# Unit tests for SearchableText (searchabletext.py)
#

import unittest
import os
from searchabletext import SearchableText
from app import RESOURCE_PATH, TEXT_FILES


class TestSearchableText(unittest.TestCase):

    def setUp(self):
        self.st_0 = SearchableText(os.path.join(RESOURCE_PATH, TEXT_FILES[0]))
        self.st_1 = SearchableText(os.path.join(RESOURCE_PATH, TEXT_FILES[1]))

    def test_id(self):
        """
        Verify that a consistent id is generated from the provided text
        """
        self.assertEqual(self.st_0.get_id(), '121b425579e19849')

    def test_two_words_same_sentence_same_line(self):
        """
        Verify that two words on the same line can be matched to the same sentence
        """
        QUERY = "beacon"
        EXPECTED = {
            "query_text": "beacon",
            "number_of_occurrences": 2,
            "occurrences": [
                {
                    "line": 3,
                    "start": 17,
                    "end": 23,
                    "in_sentence": "This momentous decree came as a great beacon light of beacon "
                                   "hope to millions of Negro slaves who had been seared in the "
                                   "flames of withering injustice."
                },
                {
                    "line": 3,
                    "start": 33,
                    "end": 39,
                    "in_sentence": "This momentous decree came as a great beacon light of beacon "
                                   "hope to millions of Negro slaves who had been seared in the "
                                   "flames of withering injustice."
                }
            ]
        }
        self.assertDictEqual(self.st_1.process_query(QUERY), EXPECTED)

    # def test_example_query(self):
    #     """
    #     Verify that the provided example "Now is" returns expected results
    #     """
    #     QUERY = "Now is"
    #     EXPECTED = {
    #         "query_text": "Now is",
    #         "number_of_occurrences": 3,
    #         "occurrences": [
    #             {
    #                 "line": 45,
    #                 "start": 17,
    #                 "end": 23,
    #                 "in_sentence": "Now is the time to rise from the dark and desolate valley of "
    #                                "segregation to the sunlit path of racial justice."
    #             },
    #             {
    #                 "line": 46,
    #                 "start": 62,
    #                 "end": 68,
    #                 "in_sentence": "Now is the time to open the doors of opportunity to all of "
    #                                "God's children."
    #             },
    #             {
    #                 "line": 48,
    #                 "start": 1,
    #                 "end": 7,
    #                 "in_sentence": "Now is the time to lift our nation from the quicksands of "
    #                                "racial injustice to the solid rock of brotherhood."
    #             }
    #         ]
    #     }
    #     self.assertDictEqual(self.st_0.process_query(QUERY), EXPECTED)
