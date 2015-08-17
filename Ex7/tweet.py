#############################################################
# FILE: tweet.py
# WRITER: Eran Nussinovitch a.k.a ednussi 302186408
# EXERCISE : intro2cs ex7 2013-2014
# Description:
# Contains the inner class Tweet we created and its inner function
# Addiotional information is included in each function
#############################################################

from geo import Position
from re import sub

# Inital Values for get_sentiment:
INITIAL_SUM_SENTI_VALUE = 0
INITIAL_COUNT_VALUE = 0


class Tweet:

    
    def __init__(self, text, time, lat, lon):
        """ defying the inner useable variables of the class"""
        self.__text = text
        self.__time = time
        self.__lat = lat
        self.__lon = lon


    def get_words(self):
        """Return the words in a tweet, not including punctuation.
        """
        # using sub to change all None alphebatic character with spaces
        # than turn to lowercase and split
        return sub('[^ a-z A-Z]', ' ', self.__text).lower().split()


    def get_text(self):
        """Return the text of the tweet."""
        return self.__text


    def get_time(self):
        """Return the datetime that represents when the tweet was posted."""
        return self.__time


    def get_location(self):
        """Return a position (see geo.py) that represents
        the tweet's location."""
        return Position(self.__lat, self.__lon)


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.get_text() == other.get_text() and
                    self.get_location() == other.get_location() and
                    self.get_time() == other.get_time())
        else:
            return False


    def __str__(self):
        """Return a string representing the tweet."""
        return '"{0}" @ {1} : {2}'.format(self.get_text(),
                                          self.get_location(),
                                          self.get_time())


    def __repr__(self):
        """Return a string representing the tweet."""
        return 'Tweet({0}, {1}, {2}, {3})'.format(
            *map(repr,(self.get_text(),
                       self.get_time(),
                       self.get_location().latitude(),
                       self.get_location().longitude())))


    def get_sentiment(self, word_sentiments):
        """ gets in a dictionary "word_sentiments"
        and return a sentiment representing the degree of positive or negative
        sentiment in the given tweet, averaging over all the words in the tweet
        that have a sentiment value. 
        """

        # Initializing the function's variables
        sum_senti = INITIAL_SUM_SENTI_VALUE 
        count = INITIAL_COUNT_VALUE

        # check for every word in the tweet if its in the dict
        # sum up all values and divide by sum of count to get avrege
        for word in self.get_words():
            if word in word_sentiments:
                sum_senti += word_sentiments[word]
                count += 1
                
        if count != 0:
            return sum_senti / count
        else:
            return None
