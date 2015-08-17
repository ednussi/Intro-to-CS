#############################################################
# FILE: nation_mood.py
# WRITER: Eran Nussinovitch a.k.a ednussi 302186408
# EXERCISE : intro2cs ex7 2013-2014
# Description:
# Contains functions which determine what is the most talktive state,
# avreging the sentiments and grouping them by hour
# Addiotional information is included in each function
#############################################################

from data import load_tweets
from geo_tweet_tools import group_tweets_by_state

# Inital Values for Functions:
# for most_talkative_state function:
INITIAL_MOST_TWEETS_VALUE = 0
INITIAL_COUNTRY_WITH_MOST_TWEETS = None

# for average_sentiments function:
INITIAL_STATE_SENTI_SUM = 0
INITIAL_STATE_TWEET_COUNT = 0


def most_talkative_state(tweets, find_state):
    """ Calculate for every state in the dictionary which has the most tweets

    Arguments:
    tweets -- a sequence of tweet abstract data types
    find_state -- A function that takes a tweet and returns the name
    of the state closest to the given tweet's location.
    
    Returns:
    Return the state that has the largest number of tweets containing term.

    """
    
    # Initializing the function's variables
    most_tweets = INITIAL_MOST_TWEETS_VALUE
    state_with_most_tweets = INITIAL_COUNTRY_WITH_MOST_TWEETS
    states_dict = group_tweets_by_state(tweets, find_state)

    # for every state determent if the sate has more or less tweets
    for state in states_dict.keys():
        if len(states_dict[state]) > most_tweets:
            most_tweets = len(states_dict[state])
            state_with_most_tweets = state
    
    return state_with_most_tweets


def average_sentiments(tweets_by_state, word_sentiments):
    """Calculate the average sentiment of the states by averaging over all
    the tweets from each state. Return the result as a dictionary from state
    names to average sentiment values (numbers).
    
    Arguments:
    tweets_by_state -- A dictionary from state names to lists of tweets
    word_sentiments -- A dictionary whith words as keys and floats which
    represent the values of the sentiments of the word

    Returns:
    Return the result as a dictionary from state
    names to average sentiment values (numbers).

    Comment:
    If a state has no tweets with sentiment values, it is leaved out of the
    dictionary entirely.It does NOT include states with no tweets,
    or with tweets that have no sentiment, as 0.
    0 represents neutral sentiment, not unknown sentiment.
    """

    # Initalizing an empty dictionary
    states_by_senti_avrg_dict ={}
    for state in tweets_by_state.keys():
        # Initializing the function's variables
        state_senti_sum = INITIAL_STATE_SENTI_SUM
        state_tweet_count = INITIAL_STATE_TWEET_COUNT
        # avrege the tweet's senti for every word which appears in
        # the word_sentiments dict
        for tweet in tweets_by_state[state]:
            tweet_senti = tweet.get_sentiment(word_sentiments)
            if tweet_senti is not None:
                state_senti_sum += tweet_senti
                state_tweet_count += 1
                
        if state_tweet_count != 0:
            states_by_senti_avrg_dict[state] = (state_senti_sum /
                                                state_tweet_count)            
    return states_by_senti_avrg_dict
                       

def group_tweets_by_hour(tweets):
    """ Creates and arrange tweets in a list by the hour it was posted
    The indexes of the returned list represent the hour when they were posted
    - the integers 0 through 23.

    Arguments:
    tweets -- A list of tweets to be grouped

    Returns:
    Return a list of lists of tweets that are grouped by the hour
    they were posted.
    """
    
    # creating the empty list and appending empty lists in each hour
    tweets_by_hour = []
    for index in range(24):
        tweets_by_hour.append([])

    # appending the tweet in the correct place by the hour it was posted
    for tweet in tweets:
        tweets_by_hour[tweet.get_time().hour].append(tweet)

    return tweets_by_hour
        


