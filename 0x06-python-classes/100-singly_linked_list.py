#!/usr/bin/python3

""" A blueprint representation of A Node and a SinglyLinked List

A Node constitutes of two members: data and next. data(int) holds the value
of the Node, while next(Node) can be None or Node type

A SinglyLinkedList represents a list of Nodes chained
together starting from a head
"""


class Node:
    """a class Node that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """ initializing object data

        Args:
            data(int): Node data
            next_node(Node): next node in chain
        """
        self.data = data
        self.next_node = next_node

    # define setters and getters for private attributes

    @property
    def data(self):
        ''' getter'''
        return self.__data

    @data.setter
    def data(self, data):
        '''setter'''
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """getter """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """setter"""
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """a class SinglyLinkedList that defines a singly linked list"""

    def __init__(self):
        """ Initialization LinkedList data"""
        self.__head = None

    def sorted_insert(self, value):
        """ inserts a new Node into the correct sorted
            position in the list (increasing order) """
        # empty list or smallest data
        if self.__head is None or self.__head.data > value:
            self.__add_node(value)
        else:
            head_copy = self.__head     # save reference to first node
            while head_copy.next_node is not None:
                if head_copy.next_node.data >= value:
                    new_node = Node(value, head_copy.next_node)
                    head_copy.next_node = new_node
                    return
                head_copy = head_copy.next_node
            self.__add_node_end(value)      # largest data

    def __add_node(self, value):
        """add node at the beginning of linked list"""
        if self.__head is None:     # empty list
            self.__head = Node(value)
        else:
            head_copy = self.__head
            self.__head = Node(value, head_copy)

    def __add_node_end(self, value):
        """add a node at the end of a linked list"""
        if self.__head is None:     # if node list is empty
            self.__add_node(value)
        first_node = self.__head    # store reference to first node
        while self.__head.next_node:
            self.__head = self.__head.next_node    # get last node

        self.__head.next_node = Node(value)     # add new node to end of list
        self.__head = first_node    # update heead node

    def __str__(self):
        """print the string representation of a Singly linked list"""
        if not self.__head:    # empty list
            return ''

        head = self.__head
        list_str = ''
        while head.next_node:
            list_str += f"{head.data}\n"
            head = head.next_node
        list_str += f"{head.data}"
        return list_str
