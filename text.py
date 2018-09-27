#
# StringLocator - 24 hour programming challenge
#
# [text.py]
# Text file loading and search algorithms
#

from nltk.tokenize import sent_tokenize
from nltk.tokenize import PunktSentenceTokenizer
import re


TEXT_PATH = './resources/text/king-easy-test.txt'


class SearchableText:
    def __init__(self, filename):
        # TODO: is there a way to search the text without loading it? (scalability)

        with open(filename) as f:
            self.text = f.read()
        self.boundaries = PunktSentenceTokenizer().span_tokenize(self.text)

        # debug 1
        sentences = sent_tokenize(self.text)
        counter = 0
        for s in sentences:
            print('[{}]'.format(counter))
            print(s)
            counter = counter + 1

    def text(self):
        return self.text

    def last_boundary(self):
        # debug 2
        for b in self.boundaries:
            print(b)
        return b


class QueryResult:
    def __init__(self, query):
        self.query = query


s = SearchableText(TEXT_PATH)
q = QueryResult("beacon")


# grab sentence from text and replace CRLF with spaces
print(re.sub(r"\r?\n", " ", s.text[slice(*s.last_boundary())]))
