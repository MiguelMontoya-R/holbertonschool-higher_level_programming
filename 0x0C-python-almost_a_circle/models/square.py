#!/usr/bin/python3
""" Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """[summary]

    Args:
        Rectangle ([type]): [description]
    """

    def __init__(self, size, x=0, y=0, id=None):
        """[summary]

        Args:
            size ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.width

    @size.setter
    def size(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """[summary]
        """
        k = ['id', 'size', 'x', 'y']

        if args:
            for i in range(len(args)):
                setattr(self, k[i], args[i])
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        dic = {'id': self.id,
               'size': self.size,
               'x': self.x,
               'y': self.y}
        return dic
