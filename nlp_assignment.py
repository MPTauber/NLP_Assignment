## py -3 -m venv nlp_venv
## nlp_venv/scripts/activate
## pip install textblob
## py -m textblob.download_corpora
from textblob import TextBlob
import nltk
#nltk.download("stopwords") # only have to do this once
from nltk.corpus import stopwords
from pathlib import Path