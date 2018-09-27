#
# StringLocator - 24 hour programming challenge
#
# [text.py]
# Text file loading and search algorithms
#


# loads text from a file
# TODO: is there a way to search the text without loading it? (scalability)
def load(filename):
    with open(filename) as f:
        return f.read()