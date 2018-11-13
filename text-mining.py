import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
# sentence = "I don't like reading classic books because they are boring."
# score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# print(score)

import imdbpie
from imdbpie import Imdb

imdb = Imdb()
print(imdb.search_for_title("The Pink Panther")[0])
reviews = imdb.get_title_user_reviews("tt0383216")

# import pprint
# pprint.pprint(reviews)

print(reviews['reviews'][0]['author']['displayName'])
print(reviews['reviews'][0]['reviewText'])

import string
print(string.punctuation)

# for line in reviews:
#     if line.

