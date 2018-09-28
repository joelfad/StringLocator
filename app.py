#
# StringLocator - 24 hour programming challenge
#
# [app.py]
# Starting point of application, contains REST route definitions
#


from flask import Flask, url_for, jsonify
from searchabletext import SearchableText

TEXT_PATH = './resources/text/king-i.txt'

app = Flask(__name__)
st = SearchableText(TEXT_PATH)

@app.route('/')
def index():
    # TODO: Return API documentation
    return 'index'


@app.route('/search')
def search():
    # TODO: Return API documentation
    # debug: confirm jsonify can handle dictionaries
    return jsonify(
        {
            "apples": 1,
            "pears": 2,
            "kiwis": 5
        }
    )


# sample return JSON
@app.route('/search/<query>')
def find(query):
    return jsonify(st.process_query(query))


# sample showing URLs
with app.test_request_context():
    print(url_for('index'))
    print(url_for('search'))
    print(url_for('search', next='/'))
    print(url_for('find', query='Now'))


if __name__ == '__main__':
    app.run()
