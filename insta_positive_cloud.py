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



blob = TextBlob(Path("positive_survey_3_17.txt").read_text())

items = blob.word_counts.items() # list of tuples with every word plus their corresponding freuqency in the text
items_list = [item for item in items]
# Get the 15 most common words
from operator import itemgetter

sorted_items = sorted(items_list, key = itemgetter(1), reverse=True)  # the 1 stands for [1], so the second part of the object
# reverse reverses sorted order and shows the highest numbers first. 

print(sorted_items)

sorted_items = dict(sorted_items)


### Make list into string for wordcloud


#######
# Now make word cloud
from wordcloud import WordCloud
import imageio

import matplotlib as plt

mask_image = imageio.imread("mask_heart.png")
wordcloud = WordCloud(font_path="LeagueGothic-Regular" ,colormap = "Wistia", mask= mask_image, background_color="#0e3426")
wordcloud = wordcloud.fit_words(sorted_items)

wordcloud = wordcloud.to_file("Q2_survey_3_17.png")

print("done")