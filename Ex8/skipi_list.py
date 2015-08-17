#############################################################
# FILE:skipi_list.py
# WRITER: Eran Nussinovitch a.k.a ednussi 302186408
# EXERCISE : intro2cs ex8 2013-2014
# Description:
# Contains the Class "SkipiList" and its inner functions
# Additional information is provided in each function
#############################################################


from sllist import SkipiNode as Node


class SkipiList:
    """
    This class represents a special kind of a doubly-linked list
    called a SkipiList. A SkipiList is composed of Nodes (SkipiNode from
    sllist).cIn addition to the data, each Node has one pointer to the
    next Node in the list, and another pointer to the prev-prev Node in the
    list (hence the name "skipi"). The only data members the class contains
    are the head and the tail of the list.
    """
    def __init__(self):
        """Constructs an empty SkipiList.

        Arguments:
        no args - self

        Return:
        no return
        """
        self.head = None
        self.tail = None

    def add_first(self, data):
        """Adds an item to the beginning of a list.

        Arguments:
        data - the item to add

        Return
        None - notice the node is created
        """
        # In case the list is empty
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            return None
        else:
            # create the new node as head with proper links
            self.head = Node(data, self.head, None)
            # In case list has 2 or more nodes
            if self.head.next.next is not None:
                self.head.next.next.skip_back = self.head
            return None

    def remove_first(self):
        """Removes the first Node from the list and return its data.

        Arguments:
        no args - self

        Return:
        Returns that data of the removed node
        """
        # In case list is empty
        if self.head is None:
            return None
        else:
            # keep data and change the head of list
            removed_head_data = self.head.data
            # In case list is only 1 node
            if self.head == self.tail:
                self.head = None
                self.tail = self.head
            else:
                # change the head of list
                self.head = self.head.next
                # In case original skipilist has more than 2 nodes erase 3rd skipback
                if self.head.next is not None:
                    self.head.next.skip_back = None

        return removed_head_data

    def add_last(self, data):
        """Adds an item to the end of a list.

        Arguments:
        data - the item to add

        Return:
        no return - notice the node was created
        """
        # In case list is empty
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            # In case original skipilist has 1 node
            if self.head.next is None:
                self.head.next = Node(data)
                self.tail = self.head.next
            else:
                # In case original skipilist has more than 2 nodes
                self.tail.next = Node(data)
                if self.tail.skip_back is None:
                    self.tail.next.skip_back = self.head
                else:
                    self.tail.next.skip_back = self.tail.skip_back.next
                self.tail = self.tail.next

    def remove_last(self):
        """Removes the last Node from the list and return its data.

        Arguments:
        no args - self

        Returns:
        The data of the removed node
        """
        # In case list empty
        if self.head is None:
            return None
        else:
            # remember the data
            removed_last_data = self.tail.data
            # In case is only 1 element
            if self.head.next is None:
                self.head = None
                self.tail = self.head
            else:
                # In case only 2 elements long
                if self.tail.skip_back is None:
                    self.head.next = None
                    self.tail = self.head
                else:
                    # In case 3 and above elements long
                    self.tail.skip_back.next.next = None
                    self.tail = self.tail.skip_back.next

        return removed_last_data

    def remove_node(self, node):
        """Removes a given Node from the list, and returns its data.

        Arguments:
        node to be removed

        Returns:
        the removed node's data

        Comments:
        Assuming the given node is in the list. Runs in O(1).
        """

        removed_node_data = node.data
        # In case it is the only node in the list
        if self.head == self.tail:
            self.head = None
            self.tail = self.head
        else:
            # In case node is in head
            if node == self.head:
                return self.remove_first()
            # In case node is in last place
            if node == self.tail:
                return self.remove_last()
            # In case node is in seconde place
            if node.skip_back is None and self.head.next == node:
                # In case only 2 in list
                if node.next is None:
                    self.tail = self.head
                    self.head.next = None
                # more than 2 in list
                else:
                    # In case exactly 3 in list
                    if node.next.next is None:
                        node.next.skip_back = None
                        self.head.next = node.next
                    # in case 4 or more
                    else:
                        node.next.skip_back = None
                        node.next.next.skip_back = self.head
                        self.head.next = node.next
            else:
                # In case the node is in 3rd or more place
                    # one before last
                    if node.next.next is None:
                        node.next.skip_back = node.skip_back
                        node.skip_back.next.next = node.next
                    else:
                        # Somewhere in the middle
                        node.next.skip_back = node.skip_back
                        node.next.next.skip_back = node.skip_back.next
                        node.skip_back.next.next = node.next

        return removed_node_data

    def __getitem__(self, k):
        """Returns the data of the k'th item of the list.
        If k is negative return the data of k'th item from the end of the list.
        If abs(k) > length of list raise IndexError.

        Arguments:
        the k'th item which we want its data

        Returns:
        Returns the data of the k'th item of the list.
        """

        if self.head is None:
            return None

        def check_length(self):
            """Returns the length of the list for a given non empty SkipiList

            Arguments:
            no args - self

            Returns:
            Returns the length of the list
            """
            # Initialize node amount for a non empty list and increase its size
            # for every run until end of list
            nodes_amount = 1
            current_node = self.head
            while current_node.next is not None:
                nodes_amount += 1
                current_node = current_node.next
            return nodes_amount

        list_length = check_length(self)
        # In case k is not of proper value
        if (0 < k and k >= list_length) or (k < 0 and abs(k) > list_length):
            raise IndexError

        # in case k is negative set the proper reference
        if k < 0:
            k = list_length + k

        # runs on the list to get to the k element
        current_node = self.head
        for node in range(k):
            current_node = current_node.next

        return current_node.data






