#!/usr/bin/python3
"""lookup function module"""


class MyList (list):
    """ mylist clas inhirates from list all attr"""
    def print_sorted(self):
        """print_sorted method orints list in ascending order"""
        lis = self[:]
        lis.sort()
        print(lis)
