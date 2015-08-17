#############################################################
# FILE: OneLiners.py
# WRITER: Eran Nussinovitch a.k.a ednussi 302186408
# EXERCISE : intro2cs ex6 2013-2014
# Description:
# Contains 8 Functions which make operations in 1-3 line top
# Included additional details in each documantion of each function
#############################################################

from operator import mul
from itertools import groupby
from string import ascii_lowercase
from random import choice
from re import sub

def is_two_palindrome(two_pali):

    """
    The function tests if the given string is a “two palindrome” or not.
    
    Args: String of any length. The string may include
    punctuation, spaces, and other symbols
    
    return: Boolean.
    
    In case of empty list or a 1 length string returns True

    Assuming Input is legal
    """
        
    # In case empty or 1 length string 
    if two_pali == '' or len(two_pali) ==1 : return True
    
    # splits the phrase enterd into splitted workable lists
    # takes into consideration if is even or odd length
    splitted = [two_pali[index:index+len(two_pali)//2] for index in range(
        0, len(two_pali), len(two_pali)//2 + (len(
            two_pali) % 2 != 0 and 1 or 0))]
             
    # returns True if both parts are palindrome
    return True if (splitted[0] == splitted[0][::-1]  and(
        splitted[1] == splitted[1][::-1])) else False
    
def uni_sort(list1, list2):

    """
    The function combines two unsorted lists of integers into one sorted list
    
    Args: Two lists of integers.
    
    return: A sorted list in ascending order - small to big. each
    distinct integer is shown only once.

    Import Usage:
    Uses groupby from itertools which removes all duplicates in the list
    in order to avoid writing a for loop to determinte comperhasion
    between the two lists and appending only new values into a new list
    
    Assuming Input is legal
    """
        
    # adds lists, arrange in asecnding values - than remove duplicates
    return [cell for cell, _ in groupby(sorted(list1 + list2))] 




def dot_product(vector1, vector2):

    """
    The function returns the dot product of two vectors,
    represented as lists
    
    Args: Two lists (representing vectors) of integers.
    
    return: an integer – the dot product of the two input vectors.

    Import Usage:
    Uses mul from operator as a built in function to create multiplication of
    two values. used in with map it replaces creating a loop to
    mulitply each cell in one vector to the same cell in the other vector.

    Assuming Input is legal
    """
        
    # multiplying each cell of one vector with the others, and sum them up
    return sum(map(mul, vector1, vector2))



def list_intersection(list1, list2):

    """
    The function gets as input two lists of integers and returns a new list
    sorted in ascending order
    
    Args: Two (unsorted)lists of integers.
    
    return: A list of integers sorted in ascending order containing
    those integers that appear in exactly one of the input lists.

    Assuming Input is legal
    """
        
    # removes duplicates, combines only what is only in both,
    # creates a list of that and sorts it
    return sorted(list(set(list1) & set(list2)))



def list_difference(list1, list2):

    """
    The function gets two input lists of integers, the function returns
    a list sorted in ascending order
    
    Args: Two (unsorted)lists of integers.
    
    return: A list of integers sorted in ascending order containing
    those integers that appear in exactly one of the input lists

    Assuming Input is legal
    """
    
    # removes duplicates, combines only what is not in both,
    # creates a list of that and sorts it
    return sorted(list(set(list1) ^ set(list2)))

def random_string(length):

    """
    The function generates a random string of a given length
    
    Args: An integer "length" denoting the length of
    the output random string.
    
    return: A random string of length "length".

    Import Usage:
    Uses ascii_lowercase from string in order to shorten and make sure
    the random choice creation is only from the exact lower cases
    from ascii code
    Uses choice from random in order to pick randomly from the entire
    ascii code mentioned above and avoiding writing a function
    which uses a picked logic in order to pick one character
    from a string randomly
    
    Assuming Input is legal
    """
        
    # picks randomly "length" letters from ascii's lower case letters and
    # joins them without spaces into a string
    return ''.join(choice(
       ascii_lowercase) for index in range(length))


def word_mapper(input_string):

    """
    The function returns a dictionary mapping from the words in
    the input text to their number appearances. 
    
    Args: A string of words separated by whitespace
    and/or punctuation marks.
    
    return: A dictionary containing a mapping between words
    (as keys) and the number of times they appear in the
    original input string (as value).

    Import Usage:
    using sub from re in order to replace each punctuation mark with a space
    so a workable string is given. used insted of creating a function which
    loops through the entire text and checks for every given punction
    mark in it.
    
    Assuming Input is legal
    """
        
    # removing all punctuation marks, turn upper to lower case and splits
    removed_punc_str = (((sub(r'\_',' ' ,sub(
        r'\W',' ' , input_string)))).lower().split())

    # creates list of itereables containning number of repeted time
    # and the word itself, removes dupliactes and turn into dicitionary
    return dict(set([(
        index, removed_punc_str.count(index)) for index in removed_punc_str]))

    
def gimme_a_value(function, value):

    """
    The function returns the current value from a generator which works
    based on a given function put in and an initial value to start with
    
    Args: A function, and an initial value
    
    return: The next element in the sequence generated by the given function
    applying to the previous element.
    The first returned value is the initial value 
    
    Assuming Input is legal
    """
    
    # for each run after first use function on current value and return it
    while True:
        yield value
        value = function(value)



