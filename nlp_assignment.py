## py -3 -m venv nlp_venv
## nlp_venv/scripts/activate
## pip install textblob
## py -m textblob.download_corpora
# pip install wordcloud
# pip install imageio


from textblob import TextBlob
import nltk
#nltk.download("stopwords") # only have to do this once
from nltk.corpus import stopwords
from pathlib import Path

stops = stopwords.words("english")

blob = TextBlob(Path("book of John text.txt").read_text())
nouns = blob.noun_phrases

items = blob.word_counts.items() # list of tuples with every word plus their corresponding freuqency in the text

items_not_in_stops = [item for item in items if item[0] in nouns if item[0] not in stops]
#######
# Get the 15 most common words
from operator import itemgetter

sorted_items = sorted(items_not_in_stops, key = itemgetter(1), reverse=True)  # the 1 stands for [1], so the second part of the object
# reverse reverses sorted order and shows the highest numbers first. 

top15 = dict(sorted_items[:16])
print(top15)


### Make list into string for wordcloud


#######
# Now make word cloud
from wordcloud import WordCloud
import imageio

import matplotlib as plt

mask_image = imageio.imread("mask_oval.png")
wordcloud = WordCloud(colormap = "PuRd", mask=mask_image, background_color="black")
wordcloud = wordcloud.fit_words(top15)

wordcloud = wordcloud.to_file("BookOfJohnWordCloud.png")

print("done")