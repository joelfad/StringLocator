#
# StringLocator - 24 hour programming challenge
#
# [searchabletext.py]
# Text file loading and search algorithms
#

# Note: The tokenizer appears to have trouble interpreting sentences that contain quotes: ""
#       In a future iteration, a more accurate model could be trained/used.
from nltk.tokenize import PunktSentenceTokenizer
import re
import hashlib
import sys


class SearchableText:
    """
    Represents a body of text which can be searched for occurrences of a query. Reduces the
    number of times the text is loaded and traversed
    """

    def __init__(self, file_path):
        """
        Initialize searchable text object with plaintext file.

        :param file_path: string, path to file
        """
        # load file
        with open(file_path, 'r') as f:
            try:
                self.text = f.read()
                self.text_lines = self.text.split('\n')
            except IOError as e:
                print("Error: Unable to read file: {}".format(e))
                sys.exit(1)

        # detect sentence boundaries
        self.boundaries = list(PunktSentenceTokenizer().span_tokenize(self.text))

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

        # start with the first sentence boundary
        self.current_boundary = 0

        lines_of_text = self.text.split('\n')

        pattern = re.compile(query_text)
        for line_number, line in enumerate(lines_of_text, 1):

            # matches are returned in order found, left to right
            matches = re.finditer(pattern, line)
            for m in matches:
                match_index = chars_on_prev_lines + m.start()
                occurrences.append(
                    {
                        "line": line_number,        # line numbers start at 1
                        "start": m.start() + 1,     # first character of occurrence
                        "end": m.end() + 1,         # character immediately after occurrence
                        "in_sentence": self._find_sentence(match_index)
                    }
                )

            # add characters from current line before proceeding to the next
            chars_on_prev_lines = chars_on_prev_lines + len(lines_of_text[line_number - 1]) + 1

        return occurrences

    def _find_sentence(self, match_index):
        """
        Retrieves the sentence a match belongs to.

        :param char_index: int, index (from beginning of file starting at 0) of first character of match
        :return: string, sentence containing match
        """

        # iterate through the lower and upper index bounds of each sentence
        # beginning with the same sentence as the last method call
        for boundary in self.boundaries[self.current_boundary:]:

            # TODO: Look for edge cases in here (e.g. a query that somehow lands between sentences)

            # check if match index is within the current sentence boundary
            if match_index in range(*boundary):
                # grab sentence from text and replace CRLF with spaces
                return re.sub(r"\r?\n", " ", self.text[slice(*boundary)])
            else:
                # advance to next sentence
                self.current_boundary = self.current_boundary + 1
