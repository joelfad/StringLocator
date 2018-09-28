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
        """
        Initialize searchable text object with plaintext file.

        :param file_path: string, path to file
        """
        # load file
        # TODO: Handle errors here if file is not found...
        with open(file_path, 'r') as f:
            self.text = f.read()

        # detect sentence boundaries
        self.boundaries = PunktSentenceTokenizer().span_tokenize(self.text)

        # create unique 16-bit identifier from text
        self.id = hashlib.md5(self.text.encode('utf-8')).hexdigest()[16:]

    def get_id(self):
        """
        Returns unique id generated from document's contents.

        :return: string, md5 hash of document text
        """
        return self.id

    def process_query(self, query_text):
        """
        Queries document for provided string and aggregates results in a dictionary.

        :param query_text: string, to search document for
        :return: dictionary, with the following schema:
            {
                "query_text": <string used for query>,
                "number_of_occurrences": <results found>,
                "occurrences": [
                    {
                        "line": <line number of result>,
                        "start": <index of result's first character>,
                        "end": <index of character immediately after result>,
                        "in_sentence": <sentence result was found in>
                    },
                    {
                        ...
                    }
                ]
            }
        """

        occurrences = self._find_occurrences(query_text)
        return {
            "query_text": query_text,
            "number_of_occurrences": len(occurrences),
            "occurrences": occurrences
        }

    def _find_occurrences(self, query_text):
        """
        Internal implementation of "process_query" method. This is where the hard work
        of searching and indexing the document text takes place.

        :param query_text: string, to search document for
        :return: list of dictionaries containing detailed results (see "process_query" above)
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

        :param char_index: int, index (from beginning of file starting at 0) of first character of match
        :return: sentence the match belongs to
        """

        print("OUTSIDE")
        # iterate through each sentence
        for boundary in self.boundaries:

            # debug
            # print(boundary)

            # TODO: Look for edge cases in here (e.g. a whitespace search that is between sentences)

            # handle all matches in current sentence before advancing
            print("FOR LOOP")
            while char_index in range(*boundary):
                print("WHILE LOOP")

                # debug
                # print("{} is in the range{}\n".format(char_index, boundary))

                # grab sentence from text and replace CRLF with spaces
                yield re.sub(r"\r?\n", " ", self.text[slice(*boundary)])
