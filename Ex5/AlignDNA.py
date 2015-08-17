#############################################################
# FILE: AlignDNA.py
# WRITER: Eran Nussinovitch a.k.a ednussi
# EXERCISE : intro2cs ex5 2013-2014
# Description
# Two function used to determinte the score of 2 aligned starnds of DNA
# According to a given logic score, and a function which detremints
# what is the best strand possible to create from 2 given starnds and a
# score logic
#############################################################

DEFAULT_MATCH = 1
DEFAULT_MISMATCH = -1
DEFAULT_GAP = -2
INITIAL_ALIGNMENT_SCORE = 0
LEFT_SIDE_IS_BIGGER = 1
RIGHT_SIDE_IS_BIGGER = 2
HAS_NOT_CHANGED = False
HAS_CHANGED = True

# A function which gets in 2 aligned DNA starnds of the same length
# and comperer their score according to a default or given
# logic score of mathced, mismatched, or gap found within the strands
def get_alignment_score(list1, list2, match_val = DEFAULT_MATCH,
                        mismatch_val = DEFAULT_MISMATCH,
                        gap_val = DEFAULT_GAP):
    
    # Turns the tuples into lists
    list1 = list(list1)
    list2 = list(list2)
    
    # compares the diffrent lists in each position
    alignment_score = INITIAL_ALIGNMENT_SCORE
    for cell in range(len(list1)):
        
        # in case of match
        if list1[cell] == list2[cell]:
            alignment_score += match_val
          
        # in case of gap 
        elif ((list1[cell] == "-" and list2[cell] != "-") or (
            list2[cell] == "-" and list1[cell] != "-")):
            alignment_score += gap_val

        # in case of missmatch 
        else:
            alignment_score += mismatch_val
           
    return alignment_score

# a function which takes in any two starnds of DNA -
# and returns the best possible alignment of the two lists
# following a score logic of match, mismatch, and gap between
# the strands
def get_best_alignment_score(list1, list2, match = DEFAULT_MATCH,
                             mismatch = DEFAULT_MISMATCH,
                             gap = DEFAULT_GAP):
    # Turns the tuples into lists and creates new empty list
    list1 = list(list1)
    list2 = list(list2)
    new_list = []

    # In case one of the lists is empty autimatically create
    # a list of '-' in the proper length and returns it with score
    if list1 == [] or list2 == []:
        if list1 == []:
            for cell in range(len(list2)):
                new_list.append('-')
            best_score = gap*len(list2)
            return (best_score, "".join(new_list), "".join(list2)) 
            
        if list2 == []:
            for cell in range(len(list1)):
                new_list.append('-')
            best_score = gap*len(list1)
            return (best_score, "".join(list1), "".join(new_list)) 
        
    # in case lists are of same size
    if len(list1) == len(list2):
        
        # in case the list are exactly the same list
        # returns score autimatically
        if list1 == list2:
            best_score = get_alignment_score(list1,list2,match,
                                             mismatch, gap)
            return (best_score, "".join(list1), "".join(list2))

        # in case there is not atlist one match of letters from
        # the DNA strand to the other - returns score without
        # the entering the recursive function
        if comparing(list1,list2)== False:
            best_score = mismatch*len(list1)
            return (best_score, "".join(list1), "".join(list2))

        # if not the same add to '-' to seconde of the strands
        # used in order to enter the recursive function
        else:
            list2.append('-')
            big_list, small_list = list2, list1
            bigger_list_place = RIGHT_SIDE_IS_BIGGER
        
    # in case the lists are of not of same length
    else:
        #determents which is the bigger list
        if len(list1) > len(list2):
            big_list, small_list = list1, list2
            bigger_list_place = LEFT_SIDE_IS_BIGGER
        else:
            big_list, small_list = list2, list1
            bigger_list_place = RIGHT_SIDE_IS_BIGGER
            
    # creates a new empty lists - to be filled later with matches
    # of the best strand
    for cell in range(len(big_list)):
        new_list.append('-')


    # enter the recursive function and give me the best alignment
    new_list = new_alignment(small_list, big_list, new_list)

    # caculate the score
    best_score = get_alignment_score(new_list, big_list, match,
                        mismatch, gap)
    #print(bigger_list_place,"cbkfinamelec")
    # making sure the starnds are returned in the right place
    if bigger_list_place == LEFT_SIDE_IS_BIGGER:
        return (best_score, "".join(big_list), "".join(new_list))
    else:
        return (best_score, "".join(new_list), "".join(big_list))

# A function witch detrements if there if atlist one match
# of letters from one strand to the other
def comparing(list1,list2):
    for cell1 in range(len(list1)):
        for cell2 in range(len(list2)):
            if list1[cell1] == list2[cell2]:
                return True
    return False


# A function which takes 2 starnds of diffrent length and creates
# the best possible alignment
def new_alignment(small_list, big_list, new_list, last_appended = 0,
                  var_num = 0):

    # comper a given index in a srand to all spaces in the other
    # strand and adds match into a new list
    has_changed = HAS_NOT_CHANGED
    for index in range(last_appended, (min( (len(big_list) - len(
        small_list) + 1 + last_appended) , len(big_list)))):

        # in case found a match 
        if small_list[var_num] == big_list[index]:
            new_list[index] = small_list[var_num]
            has_changed = HAS_CHANGED  
            last_appended = index + 1
            break

    # in case didn't find any match of the compered index
    if has_changed == HAS_NOT_CHANGED:
        new_list[last_appended] = small_list[var_num]
        last_appended += 1
            
    # exiting logic - continue untill u compered all possible indexs
    if var_num < len(small_list):
        var_num += 1
    if var_num == len(small_list):
        return new_list

    # returns the new alignment
    return new_alignment(small_list, big_list, new_list, last_appended, var_num)
