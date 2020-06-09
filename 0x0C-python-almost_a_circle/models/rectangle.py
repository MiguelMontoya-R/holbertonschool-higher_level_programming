#!/usr/bin/python3
from models.base import Base
"""Rectangle class
"""


class Rectangle(Base):
    """Class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle Class

        Args:
            width (int): attribute width for rectangle
            height ([type]): attribute height for rectangle
            x (int, optional): position in x .
            y (int, optional): position in y.
            id ([type], optional): Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        return (self.__height * self.__width)

    def display(self):
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        k = ['id', 'width', 'height', 'x', 'y']

        if args:
            for i in range(len(args)):
                setattr(self, k[i], args[i])
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)
