#
# StringLocator - 24 hour programming challenge
#
# [app.py]
# Starting point of application, contains REST route definitions
#


from flask import Flask, url_for, jsonify
import text

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/search')
def search():
    return 'search'


# sample return JSON
@app.route('/search/<query>')
def find(query):
    return jsonify(
        query_text=query,
        number_of_occurrences=3,
        occurrences=[
            {
                "line": 1,
                "start": 2,
                "end": 3,
                "in_sentence": "Test sentence."
            }
        ]
    )


# sample showing URLs
with app.test_request_context():
    print(url_for('index'))
    print(url_for('search'))
    print(url_for('search', next='/'))
    print(url_for('find', query='Now'))


if __name__ == '__main__':
    app.run()
