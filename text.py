#
# StringLocator - 24 hour programming challenge
#
# [text.py]
# Text file loading and search algorithms
#

from nltk.tokenize import sent_tokenize
from nltk.tokenize import PunktSentenceTokenizer
import re


# loads text from a file
# TODO: is there a way to search the text without loading it? (scalability)
def load(filename):
    with open(filename) as f:
        return f.read()


# small tests
text = load('resources/text/king-easy-test.txt')

sentences = sent_tokenize(text)
counter = 0
for s in sentences:
    print('[{}]'.format(counter))
    print(s)
    counter = counter + 1

pst = PunktSentenceTokenizer()

boundaries = pst.span_tokenize(text)
for b in boundaries:
    print(b)


# grab sentence from text and replace CRLF with spaces
print(re.sub(r"\r?\n?", "", text[slice(*b)]))