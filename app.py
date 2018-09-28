#
# StringLocator - 24 hour programming challenge
#
# [app.py]
# Starting point of application, contains REST route definitions
#


from flask import Flask, url_for, jsonify, request
from searchabletext import SearchableText
import os


app = Flask(__name__)

RESOURCE_PATH = './resources/text'  # File IDs
TEXT_FILES = [                      # ----------------
    'king-i.txt',                   # 121b425579e19849
    'king-easy-test.txt'            # 7a8764b75df898c1
]


# initialize and store searchable text objects
def init_searchable_texts():
    searchable_texts = dict()
    for t in TEXT_FILES:
        st = SearchableText(os.path.join(RESOURCE_PATH, t))
        searchable_texts[st.get_id()] = st
    return searchable_texts


library = init_searchable_texts()


# TODO: Handle REST errors by returning response codes (e.g. 400, 404, etc.) and redirecting...
# TODO: Deploy to Heroku (https://devcenter.heroku.com/articles/getting-started-with-python)


@app.route('/')
def index():
    # TODO: Return API documentation
    return 'index'


@app.route('/stringlocator/api/v1.0/search/<fileid>')
def search(fileid):

    # TODO: Verify file id and search for results. Handle case where there are none!

    query = request.args.get('q')

    st = library.get(fileid)
    if not st:
        return "<h1>Error: Invalid file ID</h1>"
    elif not query:
        return "<h1>Error: Missing query</h1>"

    return jsonify(st.process_query(query))


# sample showing URLs
with app.test_request_context():
    print(url_for('index'))
    print(url_for('search', fileid="121b425579e19849", q='beacon'))


if __name__ == '__main__':
    app.run()
