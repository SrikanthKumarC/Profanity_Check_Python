import re


tweets_file = open('tweets.txt', 'r')
tweets = tweets_file.readlines()

bad_words_file = open('bad_words.txt', 'r')
bad_words = bad_words_file.readline()


def get_profanity_degree(tweet, bad_words):
    no_of_bad_words = 0
    tweet_words = tweet.split()
    for bad_word in bad_words:
        if re.search(bad_word, tweet):
            no_of_bad_words += 1
    return no_of_bad_words/len(tweet_words)


def analyse_tweets(tweets, bad_words):
    for tweet in tweets:
        print(get_profanity_degree(tweet, bad_words), end=" \n")


analyse_tweets(tweets, bad_words)
