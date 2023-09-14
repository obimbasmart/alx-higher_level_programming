#!/usr/bin/python3

""" a class Student that defines a student based on name,
age"""


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

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__t a
