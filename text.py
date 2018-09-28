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

    def process_query(self, query_text):

        occurrences = self.find_occurrences(query_text)

        # debug
        # for o in occurrences:
        #     print(o)

        return {
            "query_text": query_text,
            "number_of_occurrences": len(occurrences),
            "occurrences": occurrences
        }

    def find_occurrences(self, query_text):

        occurrences = []

        pattern = re.compile(query_text)

        # keep running count of characters from previous lines (including newlines)
        # for pairing matches with sentences
        chars_on_prev_lines = 0

        lines_of_text = self.text.split('\n')
        print(lines_of_text)

        for line_number, line in enumerate(lines_of_text, 1):

            print("Searching line {}...".format(line_number))
            print("({} chars from previous lines)\n".format(chars_on_prev_lines))


            # matches are returned in order found, left to right
            matches = re.finditer(pattern, line)
            for m in matches:
                print(m)
                # print("line_number: {}".format(line_counter + 1))
                char_index = chars_on_prev_lines + m.start()
                occurrences.append(
                    {
                        "line": line_number,        # line numbers start at 1
                        "start": m.start() + 1,     # first character of occurrence
                        "end": m.end() + 1,         # character immediately after occurrence
                        "in_sentence": next(self.find_sentence(char_index))
                    }
                )

            # add characters from current line before proceeding to the next
            chars_on_prev_lines = chars_on_prev_lines + len(lines_of_text[line_number - 1]) + 1

        return occurrences

    def find_sentence(self, char_index):
        """
        Generator to pair matches with sentences
        """
        for b in self.boundaries:
            print(b)
            while char_index in range(*b):
                print("{} is in the range({}, {})\n".format(char_index, *b))
                # grab sentence from text and replace CRLF with spaces
                yield re.sub(r"\r?\n", " ", self.text[slice(*b)])


# debug - DEMO
s = SearchableText(TEXT_PATH)
r = s.process_query("This")
for o in r["occurrences"]:
    print(o)

