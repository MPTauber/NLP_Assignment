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

#from wordcloud import WordCloud
import imageio

stops = stopwords.words("english")

text = Path("book of John text.txt").read_text()
blob = TextBlob(text)

print([word for word in blob.words if word not in stops])


"""
wordcloud = wordcloud.generate(_________)
mask_image = imageio.imread("mask_oval.png")
wordcloud = WordCloud(colormap = "PuRd", masm=mask_image, background_color="white")
wordcloud = wordcloud.to_file("BookOfJohnWordCloud.png")
plt.imshow(wordcloud)"""
