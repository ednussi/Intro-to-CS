#############################################################
# FILE: geo_tweet_tools.py
# WRITER: Eran Nussinovitch a.k.a ednussi 302186408
# EXERCISE : intro2cs ex7 2013-2014
# Description:
# Contains geographic functions used to determinte
# distances and centers of polygons and tweets
# Formulas could be found on
# http://en.wikipedia.org/wiki/Centroid
# Addiotional information is included in each function
#############################################################

from geo import us_states, Position, geo_distance

# Inital Values for Functions
# for find_centroid function:
INITIAL_AREA_OF_POLYGON = 0
INITIAL_CENTER_X_POSITION = 0
INITIAL_CENTER_Y_POSITION = 0

# for find_center function:
INITIAL_SUM_OF_AREAS = 0
INITIAL_SUM_OF_X_POSITIONS = 0
INITIAL_SUM_OF_Y_POSITIONS = 0

# for find_closest_state:
INITIAL_CLOSEST_STATE_DISTANCE = float('inf')
INITIAL_CLOSEST_STATE_POSTAL = None
CENTER = 0
AREA = 1


def find_centroid(polygon):
    """Find the centroid of a polygon.

    Arguments:
    polygon -- A list of positions, in which the first and last are the same

    Returns: 3 numbers; centroid latitude, centroid longitude, and polygon area
    If a polygon has 0 area, return its first position as its centroid

    """
    # Initializing the function's variables
    area_poly = INITIAL_AREA_OF_POLYGON
    center_x = INITIAL_CENTER_X_POSITION
    center_y = INITIAL_CENTER_Y_POSITION

    # Calculate sum of x and y position, and total area
    for point in range(len(polygon)-1):

        center_x += (
            polygon[point].latitude() + polygon[point+1].latitude()) *(
            polygon[point].latitude()*polygon[point+1].longitude()-(
                polygon[point+1].latitude()*polygon[point].longitude()))

        center_y += (
            polygon[point].longitude() + polygon[point+1].longitude())*(
            polygon[point].latitude() * polygon[point+1].longitude()-(
                polygon[point+1].latitude() * polygon[point].longitude()))

        area_poly += (polygon[point].latitude() * polygon[point+1].longitude()-(
            polygon[point+1].latitude() * polygon[point].longitude()))
        
    # In case area is 0 (shape is a line or point)
    if area_poly == 0:
        return polygon[0], area_poly
    
    # Other cases - finishes the calculation
    else:
        area_poly /= 2
        center_x, center_y = center_x /(area_poly*6), center_y /(area_poly*6)
        return Position(center_x, center_y), abs(area_poly)


def find_center(polygons):
    """Compute the geographic center of a state, averaged over its polygons.
    The center is the average position of centroids of the polygons
    in polygons, weighted by the area of those polygons.

    Arguments:
    polygons -- a list of polygons

    Returns:
    A position class that determines the geographic
    center of a state, averaged over its polygons
    """
    
    # Initializing the function's variables
    sum_of_x_cordi = INITIAL_SUM_OF_X_POSITIONS
    sum_of_y_cordi = INITIAL_SUM_OF_Y_POSITIONS
    sum_of_areas = INITIAL_SUM_OF_AREAS

    # Calculate the sum of x, and y coordinates and sum of areas
    for polygon in polygons:
        poly_centroid = find_centroid(polygon)
        
        sum_of_x_cordi += poly_centroid[CENTER].latitude() * (
            poly_centroid[AREA])
        
        sum_of_y_cordi += poly_centroid[CENTER].longitude() * (
            poly_centroid[AREA])
        
        sum_of_areas += poly_centroid[AREA]

    # finishes the calculation by dividing the sum of the y and x
    # coordinates by the sum of areas
    return Position(
        sum_of_x_cordi / sum_of_areas, sum_of_y_cordi / sum_of_areas)


def find_closest_state(state_centers):
    """ a Function which using the geo_distance function (already provided)
    to calculate distance in miles between two latitude-longitude positions.

    Arguments:
    tweet -- a tweet abstract data type
    state_centers -- a dictionary from state names to positions.

    Returns:
    Returns a function that takes a tweet and returns the name of the state 
    closest to the given tweet's location.
    """

    
    def find_state(tweet):
        """A function that takes a tweet and returns the name of the state 
        closest to the given tweet's location. """
        # Initializing the function's variables
        closest_state_dist = INITIAL_CLOSEST_STATE_DISTANCE
        closest_state_postal = INITIAL_CLOSEST_STATE_POSTAL

        # checks for every state which is the closest and remembers its postal
        for state in state_centers.keys():
            if geo_distance(state_centers[state], tweet.get_location()) < (
                closest_state_dist):
                closest_state_dist = geo_distance(state_centers[state],(
                    tweet.get_location()))
                closest_state_postal = state

        return closest_state_postal
        
    return find_state


def find_containing_state(states):
    """Returns a function that takes a tweet and returns the name of the state 
    containing the given tweet's location.

    Use the geo_distance function (already provided) to calculate distance
    in miles between two latitude-longitude positions.

    Arguments:
    tweet -- a tweet abstract data type
    us_states -- a dictionary from state names to positions.

    >>> sf = Tweet("Welcome to San Francisco", None, 38, -122)
    >>> ny = Tweet("Welcome to New York", None, 41.1, -74)
    >>> find_state = find_containing_state(us_states)
    >>> find_state(sf)
    'CA'
    >>> find_state(ny)
    'NY'
    """

    
def group_tweets_by_state(tweets, find_state):
    """ Calculates which is the closest state the tweets are from
    and returns a dictionary that aggregates tweets by their nearest
    state center.

    The keys of the returned dictionary are state names, and the values are
    lists of tweets that appear closer to that state center than any other.
    
    Arguments:
    tweets -- a sequence of tweet abstract data types

    Returns:
    Return a dictionary that aggregates tweets by their nearest
    state center.
    """
    # Initialize an empty dict and for every tweet map in
    # the dictionary where the tweet is from, by creating keys
    # or adding to existing ones 
    tweets_by_states = {}
    for tweet in tweets:
        tweet_state = find_state(tweet)
        if tweet_state not in tweets_by_states.keys():
            tweets_by_states[tweet_state] = []
        tweets_by_states[find_state(tweet)].append(tweet)
        
    return tweets_by_states


