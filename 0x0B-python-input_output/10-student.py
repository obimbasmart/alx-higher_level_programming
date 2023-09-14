#!/usr/bin/python3

""" a class Student that defines a student based on name,
age - (based n 9-student.py)"""


class Student:
    """class defines a Student by name and age"""
    def __init__(self, first_name, last_name, age):
        """Initialize Student attribute
        Args:
            first_name(string): students firstname
            last_name(string): student's lastname
            age(int): age in years
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        if not attrs:
            return dict()
        return {attr: val for attr, val in self.__dict__.items()
                if attr in attrs}
