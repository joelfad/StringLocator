#
# StringLocator - 24 hour programming challenge
#
# [apidoc.py]
# API documentation displayed to user when accessing root
#


# This is the authoritative API documentation. In any conflicts between this file
# and other sources, this file shall take precedence.

API_DOC = """
StringLocator v1.0 API Documentation


Description:

StringLocator is a tool for querying text documents that are included in its library. It provides
a RESTful interface for Ctrl-f functionality (i.e. as in Google Chrome) and returns JSON. Search
results are include details about the location of matches within the file along with sentences for
context.


Endpoints:

Currently, only one endpoint is supported on port 5000: /stringlocator/api/v1.0/search/

To perform a search, a unique 16-bit file identifier and query string are required:
/stringlocator/api/v1.0/search/<file id>/?q=<query string>

A response (in JSON) will be returned as follows:
    {
        "query_text": <string used for query>,
        "number_of_occurrences": <total results found>,
        "occurrences": [
            {
                "line": <line number of result>,
                "start": <index of result's first character>,
                "end": <index of character immediately after result>,
                "in_sentence": <sentence result was found in>
            },
            {
                ...
            }
        ]
    }

If no results are found, "occurrences" will simply contain an empty list.


Examples:

GET Request:
http://127.0.0.1:5000/stringlocator/api/v1.0/search/121b425579e19849?q=struggle

JSON Response:
    {
        "query_text": "struggle",
        "number_of_occurrences": 2,
        "occurrences": [
            {
                "line": 69,
                "start": 37,
                "end": 45,
                "in_sentence": "We must forever conduct our struggle on the high plane of dignity
                               and discipline."
            },
            {
                "line": 144,
                "start": 32,
                "end": 40,
                "in_sentence": "With this faith we will be able to work together, to pray together,
                               to struggle together, to go to jail together, to stand up for freedom
                               together, knowing that we will be free one day."
            }
        ]
    }


GET Request:
http://127.0.0.1:5000/stringlocator/api/v1.0/search/121b425579e19849?q=apple

JSON Response:
    {
        "query_text": "apple",
        "number_of_occurrences": 0,
        "occurrences": []
    }
"""
