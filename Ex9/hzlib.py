#############################################################
# FILE:hzlib.py
# WRITER: Eran Nussinovitch a.k.a ednussi 302186408
# EXERCISE : intro2cs ex9 2013-2014
# Description:
# Contains the Huffman code algorithm functions
#############################################################

'''
This module contains several function for compress and decompress data, using
the Huffman code algorithm.
'''

from collections import Counter
import bisect

# MAGIC NUMBERS LIST
MAGIC = b"i2cshcfv1"

# used in join, build_canonical_codebook, compress
LENGTH = 0

# used in build_canonical_codebook, build_decodebook
KEY = 0
LEN_VALUE_TUPLE = 1

# used in build_decodebook, compress
VALUE = 1

# used in join
NOT_IN_CODEBOOK = 0

# Used in split, join,
TABLE_SIZE = 256

# used in pad, unpad
WANTED_LENGTH = 8

# used in make_huffman_tree
LETTER = 0
LETTERCOUNT = 1


def symbol_count(data):
    """ This function returns a counter dictionary which contains
    the frequencies of the diffrent charcters in the data

    Arguments:
    data - an iterable data

    Return
    a counter dict, containing the frequencies of the diffrent charcters
    in the data
    """
    return Counter(data)


def make_huffman_tree(counter):
    """ This fucntion creates a tuple represnting the huffman coeding tree.

    Arguments:
    counter - a counter dict, containing the frequencies of the
    diffrent charcters in a data

    Return
    returns a tuple represnting the huffman coeding tree.
    """

    # In case counter is empty or None
    if counter is None or len(counter) == 0:
        return None

    # sorts the list
    sorted_list = list(sorted(counter.items(), key=lambda n: n[LETTER],
                              reverse=True))
    sorted_list.sort(key=lambda n: n[LETTERCOUNT])

    # In case there is only 1 item
    if len(sorted_list) == 1:
        return sorted_list[0][LETTER]

    # In case 2 or more items
    while len(sorted_list) > 1:
        smallest = sorted_list.pop(0)
        second_smallest = sorted_list.pop(0)
        # chose how to create the new item
        if smallest[LETTERCOUNT] <= second_smallest[LETTERCOUNT]:
            new_item = ((second_smallest[LETTER], smallest[LETTER]),
                        second_smallest[LETTERCOUNT] + smallest[LETTERCOUNT])
        else:
            new_item = ((smallest[LETTER], second_smallest[LETTER]),
                        second_smallest[LETTERCOUNT] + smallest[LETTERCOUNT])

        # In case last 2 items remain and now the list is empty
        if sorted_list == []:
            return new_item[LETTER]
        # In case there are more than 2 items remain
        else:
            # make a list to compare of all the remainders frequencies
            remain_frequencies = []
            for remains in sorted_list:
                remain_frequencies.append(remains[LETTERCOUNT])

            #places the new item in the right place in the list
            insert_index = bisect.bisect(remain_frequencies,
                                         new_item[LETTERCOUNT])
            sorted_list.insert(insert_index, new_item)


def build_codebook(huff_tree):
    """ This function creates a dictionary that maps each charater
    from the given tree to a tuple which holds the length of the bits,
    and the value of the bits

    Arguments:
    huff_tree - a tuple represnting the huffman tree

    Return
    a dict - represnting the codebook of the huffman tree
    """

    # intialize an empty codebook
    huffman_codebook = {}

    # In case dict is empty
    if huff_tree is None:
        return huffman_codebook

    def recursive_builder(huff_tree, prefix=""):
        """ A help function which creates the huffman codebook
        by a given tree

        Arguments:
        huff_tree - a tuple represnting the huffman tree
        prefix - a set string that represent the needed prefix
        to add to each of the character

        Return
        a dict - represnting the codebook of the huffman tree
        """

        # Base case - check if the node represents a leaf
        if type(huff_tree) == int:
            # In case recursion started on 1 length
            if prefix == "":
                prefix = '0'
            huffman_codebook[huff_tree] = (len(prefix), int(prefix, 2))
        else:
            # reapeting conditions to adding prefix
            if huff_tree[1] is not None:
                recursive_builder(huff_tree[1], prefix + '1')
            if huff_tree[0] is not None:
                recursive_builder(huff_tree[0], prefix + '0')

        return huffman_codebook

    return (recursive_builder(huff_tree))


def build_canonical_codebook(codebook):
    """ This function creates a cannonical huffman codebook, by
    taking a normal huffman codebook and change it to a
    cannonical represntation

    Arguments:
    codebook - a dict of the normal huffman codebook

    Return
    a dict - represnting the cannonical codebook of the huffman tree
    """


    # sorts the codebook into list
    sorted_codebook = [item for item in codebook.items()]
    sorted_codebook.sort(key=lambda node: (node[LEN_VALUE_TUPLE][LENGTH], node[KEY]))

    # for each item calculate its value and insert into dictionary
    current_binary_value = 0
    for item in range(len(sorted_codebook)):
        #calculate the binary value of the item
        item_binary_value = bin(current_binary_value)[2:]
        # adds '0' in the end of the number in case it is not 8 length number
        item_binary_value += '0' * abs(
            sorted_codebook[item - 1][LEN_VALUE_TUPLE][LENGTH] -
            sorted_codebook[item][LEN_VALUE_TUPLE][LENGTH])
        # turn the binary code into its representive number
        current_binary_value = int(item_binary_value, 2)
        # insert in the item's place in the dictionary, tuple with
        # calculated num and increase the current binary value
        sorted_codebook[item] = (sorted_codebook[item][KEY],
                                 (sorted_codebook[item][LEN_VALUE_TUPLE][LENGTH],
                                  current_binary_value))
        current_binary_value += 1

    return dict(sorted_codebook)


def build_decodebook(codebook):
    """ This function creates a decodebook using a codebook.
    it switches the values and the keys and map them in a dictionary

    Arguments:
    codebook - a dictionary of the huffman codebook

    Return
    a dict - represnting decodebook for the given codebook
    """
    # Initalize an empty dict and for each key insert value as key
    # and key as value
    decoded_book = {}
    for item in codebook.items():
        decoded_book[item[VALUE]] = item[KEY]

    return decoded_book


def compress(corpus, codebook):
    """ This function compress a data given by the corpus by
    a given codebook.

    Arguments:
    codebook - a dictionary of the huffman codebook
    corpus - an iterable data

    Return
    An iterator - giving the bits of the compressed data
    """

    for item in corpus:
        # calculate the binary value of the
        binary_value = bin(codebook[item][VALUE])[2:]
        # adds '0' in the end of the number in case it is not 8 length number
        binary_value = '0' * abs(len(binary_value) - codebook[item][LENGTH]) \
                       + binary_value

        #for each number that compose the binary code yield each
        # number when asked
        for number in binary_value:
            yield int(number)


def decompress(bits, decodebook):
    """ This function decompress the data given in bits by a given decodebook

    Arguments:
    bits -an iterable data (contains 0 & 1)
    decodebook- a dictionary represnting decodebook for the given data

    Return:
    An iterator - giving the characters of the uncompressed data
    """

    #converts the data to workable string and initialize cuonting variables
    joined_bits = ''.join(map(str, bits))
    current_end = 1
    current_start = 0

    # runs on the range of all bits - and looks for each part of data
    # if it is contained within the decodebook
    for index in range(len(joined_bits)):
        key = (len(joined_bits[current_start:current_end]),
               int(joined_bits[current_start:current_end], 2))
        if key in decodebook:
            # if key is in the codebook yield the item in that place
            # and reset the search indexs
            yield decodebook[key]
            current_start = current_end
            current_end += 1
        else:
            # otherwise update count
            current_end += 1


def pad(bits):
    """ This function take bits and turn them into bytes, and in
    case bits are not 8 length it 'pads' them to complete them.

    Arguments:
    bits - an iterable data (which contains 0 & 1)

    Return
    An iterator - giving the bytes values
    """

    # In any case convert byteseq into list
    bits = [bit for bit in bits]
    # adding the 1 and join all bits into workable string
    bits.append(1)
    bits = ''.join(str(i) for i in bits)

    # run on all bits and calculate for each 8 their binary representive
    while len(bits) != 0:
        # In case it is the last byte calculate the binary num and empty list
        if len(bits) < WANTED_LENGTH:
            binary_num = int(bits + (WANTED_LENGTH - len(bits)) * "0", 2)
            bits = ()
        else:
            # as long as not last calculate the binary num
            # and cut the first 8 bits
            binary_num = int(bits[:WANTED_LENGTH], 2)
            bits = bits[WANTED_LENGTH:len(bits)]
        yield binary_num


def unpad(byteseq):
    """ This function takes in byte squences and 'unpads' them
    from the unessicery binary numbers from their 8 length
    numbers representation

    Arguments:
    bytseq - an iterator giving bytes values

    Return
    An iterator - giving the bits
    """

    # In any case turns input into list containning strings -
    # each is the binary code of each input
    bits = [str(bin(byte)[2:]) for byte in byteseq]

    # appends to new list all "corrected" to 8 length binary numbers
    new_bits = []
    for byte in bits:
        # In case the binary num is not 8 length adds 0 to left
        if len(byte) < WANTED_LENGTH:
            byte = "0" * (WANTED_LENGTH - len(byte)) + byte
        new_bits.append(byte)

    # joins the list into 1 string and yield numreical bit each time
    new_bits = ''.join(new_bits).rstrip("0")[:-1]
    for bit in new_bits:
        yield int(bit)


def join(data, codebook):
    """ This function checks if the giving data is within the given codebook
    and join the huffman codebook and that data - yielded

    Arguments:
    data - an iterator that gives bytes values
    codebook - a cannonical huffman dictionary

    Return
    An iterator - giving the values joined
    """

    joined_data = []
    # creating a table which the codebook is converted into
    for index in range(TABLE_SIZE):
        # In case the index is a key in the codebook yields its data
        # otherwise yield 0
        if index in codebook:
            joined_data.append(codebook[index][LENGTH])
        else:
            joined_data.append(NOT_IN_CODEBOOK)

    # adds the data so it could be returned together
    joined_data += data

    # yields the bytes in the data
    for datom in joined_data:
        yield datom


def split(byteseq):
    """ This function splits the huffman codebook and coded data
    from a given byte sequences given from an iterator which gives a coded
    codebook and data.

    Arguments:
    byteseq - an iterator which gives bytes represnting
    a coded codebook and data.

    Return
    A tuple - containning iterator for the data,
    and dictionary of the cannonical codebook
    """

    # Converts byteseq into list and initialize dictionary
    byteseq = [bit for bit in byteseq]
    byte_dict = {}

    # run on the table range and if the index in the byteseq
    # adds to the new dictionary
    for index in range(TABLE_SIZE):
        if byteseq[index] != 0:
            byte_dict[index] = (byteseq[index], 0)


    def byte_iterator(byteseq):
        """ help function which which creates an iterator for the compressed data

        Arguments:
        byteseq - an iterator which gives bytes represnting
        a coded codebook and data.

        Returns:
        the index place of the byte sequence
        """
        for index in range(TABLE_SIZE, len(byteseq)):
            yield byteseq[index]

    return byte_iterator(byteseq), build_canonical_codebook(byte_dict)
