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


items = blob.word_counts.items()
items_not_in_stops = [item for item in items if item[0] not in stops]

#######
# Get the 15 most common words
from operator import itemgetter

sorted_items = sorted(items_not_in_stops, key = itemgetter(1), reverse = True)

top15_items = sorted_items[:16]



top15_list = [(x[0] + " ") * x[1] for x in top15_items]

### Make list into string for wordcloud
top15_str = "" 
for x in top15_list:  
    top15_str += x

#######
# Now make word cloud
from wordcloud import WordCloud
import imageio

import matplotlib as plt

mask_image = imageio.imread("mask_oval.png")
wordcloud = WordCloud(colormap = "PuRd", mask=mask_image, background_color="white")
wordcloud = wordcloud.generate(top15_str)

wordcloud = wordcloud.to_file("BookOfJohnWordCloud.png")