#!/usr/bin/python3

"""class MyInt that inherits from int"""


class MyInt(int):
    """class inherits from int
    MyInt is a rebel: == and != are inverted"""
    def __eq__(self, other):
        "return False if equal"
        return self.real != other.real

    def __ne__(self, other):
        """return False if not equal"""
        return self.real == other.real
