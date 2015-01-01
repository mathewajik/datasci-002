import sys
import json
import re

sentiment_scores_single = {}
sentiment_scores_multi = {}

def load_scores(sentiment_file):
    for line in sentiment_file:
        word, score  = line.split('\t')
        if ' ' in word:
            sentiment_scores_multi[word] = int(score)
        else:
            sentiment_scores_single[word] = int(score)

def print_tweet_scores(tweet_file):
    for line in tweet_file:
        try:
            tweet = json.loads(line)
            if tweet.get('lang', 'xx') == 'en':
                text = tweet['text'].encode('utf-8')
                text = re.sub('[.?!"]', ' ', text).lower() # clean it
                score = 0

                for phrase in sentiment_scores_multi.keys():
                    if ' ' + phrase + ' ' in text:
                        score = score + sentiment_scores_multi.get(phrase, 0)
                        text = text.replace(phrase, '')
                
                words = text.split(' ')        
                for word in words:
                    score = score + sentiment_scores_single.get(word, 0)
                    
                print score
        except:
            pass

def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    load_scores(sentiment_file)
    print_tweet_scores(tweet_file)

if __name__ == '__main__':
    main()
