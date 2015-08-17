#############################################################
# FILE:sllist_utils.py
# WRITER: Eran Nussinovitch a.k.a ednussi 302186408
# EXERCISE : intro2cs ex8 2013-2014
# Description:
# Contains functional functions which are used on "single Linked list"
# or their nodes in order to do simple operations:
# merge lists, check for cycles, reverse list, check length,
# check if is palindrome, get middle node, checks for intersection,
# get a requested node from list or merge sort a list
#############################################################

from sllist import List, Node


def merge_lists(first_list, second_list):
    """ Merges two sorted (in ascending order) lists into one new sorted list in
    an ascending order.

    Arguments:
    Two sorted lists

    Returns:
    The resulting new list is created using new nodes
    (copies of the nodes of the given lists).

    Comments: Assumes both lists are sorted in
    ascending order. The original lists are not be modified.
    """

    # Initialize a new list and nodes which points
    # to current place in each list
    merged_list = List()
    merged_list.add_first(None)
    merged_list_node = merged_list.head
    first_list_cur_node = first_list.head
    second_list_cur_node = second_list.head

    # check the values of the current node of each list
    # and create a new node with the same data in the new merged list
    while first_list_cur_node is not None and (
            second_list_cur_node is not None):
        # current node in first list is of greater value
        if first_list_cur_node.get_data() < second_list_cur_node.get_data():
            merged_list_node.set_next(Node(first_list_cur_node.get_data()))
            first_list_cur_node = first_list_cur_node.get_next()
        else:
            # current node in second list is of greater value
            merged_list_node.set_next(Node(second_list_cur_node.get_data()))
            second_list_cur_node = second_list_cur_node.get_next()

        # advance the node for the loop
        merged_list_node = merged_list_node.get_next()

    # adding the remain nodes of the non empty list
    while first_list_cur_node is not None:
        merged_list_node.set_next(Node(first_list_cur_node.get_data()))
        merged_list_node = merged_list_node.get_next()
        first_list_cur_node = first_list_cur_node.get_next()
    while second_list_cur_node is not None:
        merged_list_node.set_next(Node(second_list_cur_node.get_data()))
        merged_list_node = merged_list_node.get_next()
        second_list_cur_node = second_list_cur_node.get_next()

    # remove the initialzed None node from the beginning
    merged_list.remove_first()

    return merged_list


def contains_cycle(sll):
    """Checks if the given list contains a cycle.

    Arguments:
    a list

    Returns:
    Returns true iff the list contains a cycle

    Comments:
    A list contains a cycle if at some point a Node in the list points to
    a Node that already appeared in the list.
    Note that the cycle does not
    necessarily contain all the nodes in the list.
    The original list class and nodes are
    not be modified.
    """

    # works only if list is not empty and more than 1 node
    if sll.head is not None and sll.head.get_next() is not None:
        # Intialize 2 runners on the "course" one is twice is faster
        first_runner = sll.head
        second_runner = sll.head
        # keep running as long as the faster runner can keep going somewhere
        while second_runner is not None and \
                        second_runner.get_next() is not None:
            # In case theyclass and nodes meet - there is a cycle
            if first_runner == second_runner.get_next().get_next():
                return True
            # move runners further
            first_runner = first_runner.get_next()
            second_runner = second_runner.get_next().get_next()
    # otherwise if loop was exited - there is no cycle
    return False


def reverse(sll):
    """Reverses the given list (so the head becomes the last element, and every
    element points to the element that was previously before it).

    Arguments:
    a list

    Returns:
    None - note the list was reversed

    Comments:
    Runs in O(n).
    No new object is created.
    """

    # In case list is empty or of 1 element
    if sll.head is None or sll.head.get_next is None:
        return None

    # Initializing 3 workable nodes
    updating_last_node = None
    flipping_node = sll.head
    updating_first_node = sll.head

    # as long as not in the end of list flip the current node
    while flipping_node is not None:
        # update what is the first node, flips the pointer of
        # the last given node, and update which the new node to be flipped
        updating_first_node = updating_first_node.get_next()
        flipping_node.set_next(updating_last_node)
        updating_last_node = flipping_node
        flipping_node = updating_first_node

    # saves the new head as the last node which was handled
    sll.head = updating_last_node

    return None


def is_palindrome(sll):
    """Checks if the given list is a palindrome.

    Arguments:
    a list

    Returns:
    Returns true iff the list is a palindrome

    Comments:
    A list is a palindrome if
    for j=0...n/2 (where n is the number of elements in the list) the
    element in location j equals to the element in location n-j.
    Note that you should compare the data stored in the nodes and
    not the node objects themselves. The original list should not be modified.
    """

    # In case list is empty or of 1 element it is palindrome
    if sll.head is None or sll.head.get_next() is None:
        return True
    if sll.head.get_next() is None:
        return True

    middle_node = get_list_middle_node(sll)
    # create a new temporary list which is half of the given list
    # and reverse its order
    half_list = List()
    half_list.head = middle_node
    reverse(half_list)

    # Initialize 2 comparing nodes 1 for each list and compare them
    original_list_compare_node = sll.head
    half_list_compare_node = half_list.head
    while original_list_compare_node is not None and \
                    half_list_compare_node is not None:
        # in case the last and first nodes of list are the same
        if original_list_compare_node.get_data() == \
                (half_list_compare_node.get_data()):
            original_list_compare_node = \
                original_list_compare_node.get_next()
            half_list_compare_node = half_list_compare_node.get_next()
        else:
            # in case a difference was found and is not palindrome
            reverse(half_list)
            return False

    reverse(half_list)
    return True


def check_length(sll):
    """Checks for a given list what's it's length and returns it
    #helper function

    Arguments:
    a list

    Returns:
    it's length
    """
    # In case list is empty
    if sll.head is None or sll is None:
        return None
    else:
        # Initialize head and counting number
        current_node = sll.head
        node_count = 1
        # as long as its not the last item keep counting
        while current_node.get_next() is not None:
            node_count += 1
            current_node = current_node.get_next()

        return node_count


def get_list_middle_node(sll):
    """finds for a non empty given list what's its middle node and return it
    #helper function

    Arguments:
    a list

    Returns:
    the middle node
    """

    # Initialize the usable parameters
    list_length = check_length(sll)
    node_count = 1
    current_node = sll.head

    # runs in list until gets to middle node
    while node_count < list_length//2:
        current_node = current_node.get_next()
        node_count += 1

    return current_node


def have_intersection(first_list, second_list):
    """Checks if the two given lists intersect.

    Arguments:
    2 lists

    Returns:
    Returns true iff the lists intersect.

    Comments:
    Two lists intersect if at some point they start to share nodes.
    Once two lists intersect they become one list from that point on and
    can no longer split apart. Assuming that both lists does not contain cycles.
    Noting that two lists might intersect even if their lengths are not equal.
    No new object is created, and niether list is modified.
    """

    # In case lists are empty
    if first_list.head is None or second_list.head is None:
        return False

    # if lists have intersection it means the last node would be the same
    # initialize updating last nodes variables
    first_list_last_node = first_list.head
    second_list_last_node = second_list.head

    # find  last nodes of each list
    while first_list_last_node.get_next() is not None:
        first_list_last_node = first_list_last_node.get_next()
    while second_list_last_node.get_next() is not None:
        second_list_last_node = second_list_last_node.get_next()

    # compare if the last nodes are the same -
    # if they are the lists have somewhere intersected
    if first_list_last_node is second_list_last_node:
        return True
    else:
        return False


def get_item(sll, k):
    """Returns the k'th element from a given list list.
    If k > list_size returns None, if k<0 returns the k element from the end.

    Arguments:
    a list
    k - an integer representing the requested node

    Returns:
    Returns the k'th element
    """

    # In case empty list
    if sll is None or sll.head is None:
        return None

    # check for the list's length
    list_length = check_length(sll)

    # In case k is not of proper value
    if (0 <= k < list_length) or (k < 0 and abs(k) <= list_length):

        # in case k is negative set the proper reference
        if k < 0:
            k = list_length + k

        # runs on the list to get to the k element
        the_k_node = sll.head
        for element in range(k):
            the_k_node = the_k_node.get_next()

        return the_k_node.get_data()
    else:
        return None


def slice(sll, start, stop=None, step=1):
    """ Returns a new list after slicing the given list from start to stop
    with a step.
    Imitates the behavior of slicing regular sequences in python.
    slice(sll, [start], stop, [step]):
    With 4 arguments, behaves the same as using list[start:stop:step],
    With 3 arguments, behaves the same as using list[start:stop],
    With 2 arguments, behaves the same as using list[:stop],
    """
    #########################################################################
    # PLEASE NOTE THIS "BONUS ASSIGNMENT" IS TAKING 2.5 POINTS OF THE GRADE!
    #########################################################################
    return List()


def merge_sort(sll):
    """Sorts the given list using the merge-sort algorithm.

    Arguments:
    a list

    Returns:
    None - notice the list was sorted according to the merge-sort algorithem

    Comments:
    Resulting list is sorted in ascending order. Resulting list
    contains the same node objects it did originally, and is stable,
    i.e., nodes with equal data should be in the same order they were in in the
    original list.
    """

    def merge_sorted_lists(list1_head, list2_head):
        """Takes in 2 sorted lists and merge them into 1 sorted list
        # helper function

        Arguments:
        2 nodes representing head of 2 diffrent lists

        Returns:
        head node of merged list
        """

        # initialize an empty node and a moving node
        merged_list_head = Node(None)
        merged_list_moving_node = merged_list_head
        # sets the merged list connection until gets to end of 1 of the lists
        while list1_head is not None and list2_head is not None:
            if list1_head.get_data() <= list2_head.get_data():
                merged_list_moving_node.set_next(list1_head)
                list1_head = list1_head.get_next()
            else:
                merged_list_moving_node.set_next(list2_head)
                list2_head = list2_head.get_next()
            merged_list_moving_node = merged_list_moving_node.get_next()

        # connect the the rest of the list which remains to the end
        if list1_head is not None:
            merged_list_moving_node.set_next(list1_head)
        else:
            merged_list_moving_node.set_next(list2_head)
        return merged_list_head.get_next()

    def reverse_two_nodes(head_of_2nodes):
        """Takes in a node which is connected to another node and reverse
        their links
        # helper function

        Arguments:
        a head node of a pair

        Returns:
        the new first node after they were reversed
        """
        #
        new_first_node = head_of_2nodes.get_next()
        head_of_2nodes.get_next().set_next(head_of_2nodes)
        head_of_2nodes.set_next(None)

        return new_first_node

    def merge_sort_recursive(node):
        """The main function of merge-sort which takes in a head node of a list
        and sort the rest of the list and returns the merged sorted list
        # helper function

        Arguments:
        head node of a list

        Returns:
        the merged sorted list
        """

        # Base Cases:
        # In case one node is left after divide or gets in a None
        if node.get_next() is None or node is None:
            return node

        # In case 2 nodes are left after divide:
        if node.get_next().get_next() is None:
            if node.get_data() > node.get_next().get_data():
                return reverse_two_nodes(node)
            else:
                return node

        # count how many nodes are
        nodes_count = 0
        current_head_node = node
        while current_head_node is not None:
            nodes_count += 1
            current_head_node = current_head_node.get_next()

        # splits the list the original node was pointed to
        current_head_node = node
        splitting_counter = 0
        while splitting_counter < nodes_count//2:
            splitting_counter += 1
            current_head_node = current_head_node.get_next()

        # intialize nodes which point to each part
        remainning_list1 = node
        remainning_list2 = current_head_node.get_next()
        current_head_node.set_next(None)

        # recursive continious split
        return merge_sorted_lists(merge_sort_recursive(remainning_list1),
                                  merge_sort_recursive(remainning_list2))

    # In case list is empty or of 1 element
    if sll is None or sll.head is None or sll.head.get_next() is None:
        return None
    else:
    # Runs the merge sort algorithem on the list an initalize its new head!
        sll.head = merge_sort_recursive(sll.head)
        return None







