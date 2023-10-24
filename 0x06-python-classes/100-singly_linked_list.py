#!/usr/bin/python3
"""Module of Square"""


class Node:
    """Represents a Square, with a name."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets the value of size"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the value of size"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """gets the value of size"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the value of position"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    __head = None

    def __init__(self):
        pass

    def __str__(self):
        tmp = self.__head
        string = ''
        while tmp.next_node is not None:
            string += str(tmp.data) + '\n'
            tmp = tmp.next_node
        return string + str(tmp.data)

    def sorted_insert(self, value):
        self.__head = Node(value, self.__head)
        return

        tmp = self.__head
        while tmp.next_node is not None:
            if tmp.data >= value:
                break
            tmp = tmp.next_node
        if tmp.data == self.__head.data:
            self.__head = Node(value, self.__head)
