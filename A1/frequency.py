from __future__ import division
import sys
import json
import re


def main():
    tweet_file = open(sys.argv[1])
    word_freq = {}

    for line in tweet_file:
        try:
            tweet = json.loads(line)
            if tweet.get('lang', 'xx') == 'en':
                text = tweet['text'].encode('utf-8')
                text = re.sub("[^\w\s]|_", '', text).lower()  # clean it

                words = text.split()
                for word in words:
                    word = word.strip()
                    word_freq[word] = word_freq.get(word, 0) + 1
        except:
            pass

    sum_words_freq = 0
    for word in word_freq:
        sum_words_freq += word_freq[word]

    for word in word_freq:
        print word, (word_freq[word] / sum_words_freq)

if __name__ == '__main__':
    main()
