#
# StringLocator - 24 hour programming challenge
#
# [app.py]
# Starting point of application, contains REST route definitions
#

# TODO: Move all test files to ./test subdirectory (deal with PyCharm path issues)
# TODO: Write more unit tests for search/indexing logic
# TODO: Handle invalid URLs (e.g. v2.0 of API which doesn't exist yet)
# TODO: Write unit tests for Flask API
# TODO: Deploy to Heroku (https://devcenter.heroku.com/articles/getting-started-with-python)
# TODO: Add deployment instructions to project README


from flask import Flask, jsonify, request, render_template
from searchabletext import SearchableText
from invalidusage import InvalidUsage
from apidoc import API_DOC
import os


app = Flask(__name__)

# text files to store in library for searching
RESOURCE_PATH = './resources/text'  # File IDs
TEXT_FILES = [                      # ----------------
    'king-i.txt',                   # 121b425579e19849
    'king-i-test.txt'               # 7a8764b75df898c1
]


# initialize and store searchable text objects
def init_searchable_texts():
    searchable_texts = dict()
    for t in TEXT_FILES:
        st = SearchableText(os.path.join(RESOURCE_PATH, t))
        searchable_texts[st.get_id()] = st
    return searchable_texts


# dictionary of texts, indexed by ID
library = init_searchable_texts()


@app.route('/')
def index():
    """
    Display API documentation.
    """
    return render_template('index.html', text=API_DOC)


@app.route('/stringlocator/api/v1.0/search/<fileid>')
def search(fileid):
    """
    Search a file for query text and return matches.

    :param fileid: string (in URL), unique 16-bit file identifier
    :param q: string (as a query parameter), query text
    :return: JSON, search results
    """
    query = request.args.get('q')

    st = library.get(fileid)
    if not st:
        raise InvalidUsage("Invalid file ID", 404)
    elif not query:
        raise InvalidUsage("Missing query")

    return jsonify(st.process_query(query))


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    """
    Handle misuse of the API. Turns an exception into a consumable response.

    :param error: InvalidUsage, exception with message and optional status code and/or payload
    :return: JSON, exception details
    """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run()
