import sys
import json
import collections

def main():
    tweet_file = open(sys.argv[1])
    hashtags_freq = collections.Counter()

    for line in tweet_file:
        try:
            tweet = json.loads(line)
            if tweet.get('lang', 'xx') == 'en':
                hashtags = tweet['entities']['hashtags']
                if hashtags:
                    for hashtag in hashtags:
                        hashtags_freq[hashtag['text']] += 1
        except:
            pass

    for hashtag, freq in hashtags_freq.most_common(10):
        print hashtag, freq

if __name__ == '__main__':
    main()

