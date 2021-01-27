#!/usr/bin/python3
"""Write the first class Base:"""


import json


class Base():
    """
    Base Class -

    Class Attributes:
        nb_objects (Private) - # of Base objects

    Public Instance Attributes:
        id = instance ID
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base instance with given ID or nb_objects"""
        Base.__nb_objects += 1
        if id is None:
            self.id = Base.__nb_objects
        elif type(id) is not int:
            raise TypeError("id must be an integer")
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json representation of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return(json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:"""
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w+", encoding="utf-8") as myFile:
            return myFile.write(Base.to_json_string(json_list))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        dummy = None
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 2, 0, 0, None)
        elif cls.__name__ is "Square":
            dummy = cls(1, 0, 0, None)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances:"""
        inst_list = []
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, mode="r", encoding="utf-8") as myFile:
                contents = myFile.read()
                if contents == "[]":
                    return(inst_list)
                json_string = (cls.from_json_string(contents))
                for instance in json_string:
                    inst_list.append(cls.create(**instance))
                return(inst_list)
        except FileNotFoundError:
            return (inst_list)
