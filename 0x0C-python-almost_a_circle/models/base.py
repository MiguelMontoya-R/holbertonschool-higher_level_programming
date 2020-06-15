#!/usr/bin/python3
"""Base class
"""
import json


class Base:
    """ If id is None the value is passed, but if not nb_objects is passed
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class

        Args:
            id ([type], optional): id parent. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation

        Args:
            list_dictionaries: List of dictionaries to be represented in JSON
            string
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        """save json repesentation in file

        Args:
            list_objs ([type]): List of dictionaries
        """
        new_l = []
        fn = cls.__name__ + '.json'
        if list_objs:
            for i in list_objs:
                new_l.append(cls.to_dictionary(i))
        with open(fn, 'w') as fn_2:
            fn_2.write(cls.to_json_string(new_l))

    @staticmethod
    def from_json_string(json_string):
        """[summary]

        Args:
            json_string ([type]): [description]

        Returns:
            [type]: [description]
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """[summary]

        Returns:
            [type]: [description]
        """
        if cls.__name__ == 'Rectangle':
            tmp = cls(1, 1)
        elif cls.__name__ == 'Square':
            tmp = cls(1)

        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """ Load from file
        """
        file_list = []
        try:
            with open(cls.__name__ + '.json', 'r') as f:
                file_list = cls.from_json_string(f.read())
            for k, v in enumerate(file_list):
                file_list[k] = cls.create(**file_list[k])
        except:
            pass
        return file_list
