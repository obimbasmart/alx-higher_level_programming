#!/usr/bin/python3

def multiple_returns(sentence):
    ''' function that returns a tuple with the
        length of a string and its first character.

        :Args:
            @sentence: string
        :Return: tuple
    '''
    if len(sentence) == 0:
        return (0, None)

    return (len(sentence), sentence[0])
