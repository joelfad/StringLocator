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
        # sentences = sent_tokenize(self.text)
        # counter = 0
        # for s in sentences:
        #     print('[{}]'.format(counter))
        #     print(s)
        #     counter = counter + 1

    def text(self):
        return self.text

    def last_boundary(self):
        # debug 2
        for b in self.boundaries:
            print(b)
        return b

    def query(self, query_text):
        result = {
            "query_text": query_text,
            "number_of_occurrences": 0,
            "occurrences": []
        }
        self.find_occurrences(query_text)

    def find_occurrences(self, query_text):

        result = []

        pattern = re.compile(query_text)
        line_counter = 0
        char_counter = 0

        lines_of_text = self.text.split('\n')
        print(lines_of_text)

        for line in lines_of_text:

            matches = re.finditer(pattern, line)
            for m in matches:
                print(m)
                # print("line_number: {}".format(line_counter + 1))
                result.append(
                    {
                        "line": line_counter + 1,
                        "start": m.start() + 1,
                        "end": m.end() + 1,
                        "in_sentence": "TODO"
                    }
                )

            char_counter = char_counter + len(lines_of_text[line_counter])
            line_counter = line_counter + 1

        for r in result:
            print(r)







        #
        # debug: this is what we need to build!
        #
        # query_text=query,
        # number_of_occurrences=3,
        # occurrences=[
        #     {
        #         "line": 1,
        #         "start": 2,
        #         "end": 3,
        #         "in_sentence": "Test sentence."
        #     }
        # ]
        #




        return result



s = SearchableText(TEXT_PATH)
r = s.query("beacon")


# grab sentence from text and replace CRLF with spaces
# print(re.sub(r"\r?\n", " ", s.text[slice(*s.last_boundary())]))
