#
# StringLocator - 24 hour programming challenge
#
# [app.py]
# Starting point of application, contains REST route definitions
#


from flask import Flask, url_for, jsonify
from searchabletext import SearchableText


app = Flask(__name__)

# TODO: Index texts by their ids so you can scale the service later...
TEXT_PATH = './resources/text/king-i.txt'
st = SearchableText(TEXT_PATH)


# TODO: Handle REST errors by returning response codes (e.g. 400, 404, etc.) and redirecting...


@app.route('/')
def index():
    # TODO: Return API documentation
    return 'index'


@app.route('/stringlocator/api/v1.0/search/<fileid>')
def search(fileid):
    # TODO: Verify file id and search for results. Handle case where there are none!
    return fileid


@app.route('/search/<query>')
def find(query):
    return jsonify(st.process_query(query))


# sample showing URLs
with app.test_request_context():
    print(url_for('index'))
    print(url_for('search', fileid="121b425579e19849", q='beacon'))


if __name__ == '__main__':
    app.run()
