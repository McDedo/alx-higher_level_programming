#!/usr/bin/python3

'''module: rectangle
this module contains the class Rectangle ...
'''


class Rectangle:
    '''class: Rectangle
    this is Rectangle class
    '''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''method: __init__
        initialize instance of class
        '''
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''method: set_width
        getter
        '''
        if (not isinstance(self.__width, int)) or isinstance(self.__width,

