from __future__ import division
import sys
import json
import re

sentiment_scores_single = {}
sentiment_scores_multi = {}

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}


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
    
    words = text.split()        
    for word in words:
        score = score + sentiment_scores_single.get(word, 0)

    return score

def state(tweet):
    if tweet['place']['country_code'] == 'US':
        place = tweet['place']['full_name']
        if ', USA' in place: # <state_name> , 'USA'
            state_name = place[:place.find(',')]
            for k,v in states.items():
                if v == state_name:
                    return k
        else: # <? name> , <state code>
            state_code = place[place.find(',')+1:].strip()
            return state_code

def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    load_scores(sentiment_file)
    
    state_scores = {}
    for line in tweet_file:
        try:
            tweet = json.loads(line)
            if tweet.get('lang', 'xx') == 'en':
                tweet_state = state(tweet)                
                if tweet_state != None:
                    text = tweet['text'].encode('utf-8')
                    text = re.sub('[.?!",]', ' ', text).lower() # clean it
                    
                    state_scores[tweet_state] = state_scores.get(tweet_state, 0) + score(text)
        except:
            pass

    max_score = max(state_scores.values())
    for k,v in state_scores.items():
        if v == max_score:
            print k,
            break

if __name__ == '__main__':
    main()

