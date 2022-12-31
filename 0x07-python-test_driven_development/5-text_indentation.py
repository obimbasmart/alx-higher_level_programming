"""
Write a function that prints a text with 2 new lines
after each of these characters: ., ? and :

- Prototype: def text_indentation(text):
- text must be a string, otherwise raise a TypeError exception
    with the message text must be a string
- There should be no space at the beginning or at the end of each
    printed line
- You are not allowed to import any module
"""


def text_indentation(text):
    # check if text is string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sep = ""
    for delim in ".:?":
        if delim in text:
            sep = "\n"
            break

    _str = text.replace('?', '.').replace('.', ':').split(':')

    [print("{:s}{:s}".format(item.strip(), sep)) for item in _str]
