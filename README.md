# WikipediaGame
AI using Standord NLP GloVe that plays the Wikipedia game.
Given a Wikipedia entry, reach another Wikipedia entry by clicking Wikipedia links.

Word similarity using: https://nlp.stanford.edu/projects/glove/

Download training set from http://nlp.stanford.edu/data/glove.6B.zip and extract to wiki-data/

Run using Python 3:
python main.py SOURCE DEST

Where SOURCE and DESK are the desired beginning and ending Wikipedia pages.

Python dependencies:
dataclasses
nltk (must also nltk.download("stopwords") and nltk.download("punkt"))
queue
typing

NOTE: Must use exact Wikipedia link ending for SOURCE and DEST (otherwise, program will not terminate)
