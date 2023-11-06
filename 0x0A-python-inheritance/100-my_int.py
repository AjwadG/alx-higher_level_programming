#!/usr/bin/python3
"""MyInt class module"""


class MyInt (int):
    """ MyInt clas inhirates from int all attr"""
    def __eq__(self, other):
        """over rides int == opration"""
        return (int(self) != other)

    def __ne__(self, other):
        """over rides int != opration"""
        return (int(self) == other)
