#
# StringLocator - 24 hour programming challenge
#
# [searchabletext.py]
# Text file loading and search algorithms
#

from nltk.tokenize import PunktSentenceTokenizer
import re
import hashlib


class SearchableText:
    def __init__(self, file_path):
        # load file
        with open(file_path, 'r') as f:
            self.text = f.read()

        # detect sentence boundaries
        self.boundaries = PunktSentenceTokenizer().span_tokenize(self.text)

        # create unique identifier from text
        self.id = hashlib.md5(self.text.encode('utf-8')).hexdigest()

    def get_id(self):
        print(self.id)
        return self.id

    def process_query(self, query_text):
        """
        TODO: Add documentation

        :param query_text:
        :return:
        """

        occurrences = self._find_occurrences(query_text)
        return {
            "query_text": query_text,
            "number_of_occurrences": len(occurrences),
            "occurrences": occurrences
        }

    def _find_occurrences(self, query_text):
        """
        TODO: Add documentation

        :param query_text:
        :return:
        """

        occurrences = []

        # keep running count of characters from previous lines (including newlines)
        # for pairing matches with sentences
        chars_on_prev_lines = 0

        lines_of_text = self.text.split('\n')

        pattern = re.compile(query_text)
        for line_number, line in enumerate(lines_of_text, 1):

            # debug
            # print("Searching line {}...".format(line_number))
            # print("({} chars from previous lines)\n".format(chars_on_prev_lines))

            # matches are returned in order found, left to right
            matches = re.finditer(pattern, line)
            for m in matches:

                # debug
                # print(m)

                char_index = chars_on_prev_lines + m.start()
                occurrences.append(
                    {
                        "line": line_number,        # line numbers start at 1
                        "start": m.start() + 1,     # first character of occurrence
                        "end": m.end() + 1,         # character immediately after occurrence
                        "in_sentence": next(self._find_sentence(char_index))
                    }
                )

            # add characters from current line before proceeding to the next
            chars_on_prev_lines = chars_on_prev_lines + len(lines_of_text[line_number - 1]) + 1

        return occurrences

    def _find_sentence(self, char_index):
        """
        Generator to pair matches with sentences
        """
        for boundary in self.boundaries:

            # debug
            # print(boundary)

            while char_index in range(*boundary):

                # debug
                # print("{} is in the range{}\n".format(char_index, boundary))

                # grab sentence from text and replace CRLF with spaces
                yield re.sub(r"\r?\n", " ", self.text[slice(*boundary)])
