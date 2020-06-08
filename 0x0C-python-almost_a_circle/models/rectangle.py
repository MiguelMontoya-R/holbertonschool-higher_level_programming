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
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self._y = value
