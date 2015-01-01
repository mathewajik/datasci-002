from __future__ import division
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

def score(text):
    score = 0
    for phrase in sentiment_scores_multi:
        if ' ' + phrase + ' ' in text:
            score = score + sentiment_scores_multi.get(phrase, 0)
            text = text.replace(phrase, '')
    
    words = text.split(' ')        
    for word in words:
        score = score + sentiment_scores_single.get(word, 0)

    return score

def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    load_scores(sentiment_file)
    
    missing_words = {}
    for line in tweet_file:
        try:
            tweet = json.loads(line)
            if tweet.get('lang', 'xx') == 'en':
                text = tweet['text'].encode('utf-8')
                text = re.sub('[.?!",]', ' ', text).lower() # clean it
                tweet_score = score(text)                
                
                words = text.split(' ')
                for word in words:
                    if word not in sentiment_scores_single:  
                        if word not in missing_words:
                            missing_words[word] = [0,0,0]

                        if tweet_score > 0:
                            missing_words[word][0] += 1 # No: of occurences of the word in tweets with positive sentiment
                        elif tweet_score < 0:                        
                            missing_words[word][1] += 1 # No: of occurences of the word in tweets with negative sentiment

                        missing_words[word][2] += 1 # Total no: of occurences of the word
        except:
           pass

    for word in missing_words:
        print word, ((missing_words[word][0] - missing_words[word][1]) / missing_words[word][2])

if __name__ == '__main__':
    main()

