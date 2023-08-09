#!/usr/bin/python3

"""
class FileStorage that serializes instances to a JSON file and deserializes
JSON file to instances
"""

from models.base_model import BaseModel
import json


class FileStorage:
    """
    This serves as the storage engine for the AirBnB web application,
    ensuring data persistence. It empowers us to convert the dictionary
    representation of objects into a JSON string through serialization.
    Additionally, it allows us to recreate instances of our BaseModel by
    deserializing JSON strings stored in a persistent file.

    Class Attributes:

        __file_path (str): The path to the JSON file (e.g., file.json).
        __objects (dict): An empty dictionary that stores all objects using
                        a format like <class name>.id (e.g., for a BaseModel
                        object with id=12121212, the key will be
                        BaseModel.12121212).
    Class Methods:

        all: Returns the dictionary __objects.
        new: Adds an object to __objects, using the key <obj class name>.id.
        save: Serializes the __objects dictionary and saves it to a JSON file.
        reload: Deserializes the JSON file and loads data back into the
        __objects dictionary
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """retrieves the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """stores the obj in the __objects dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """writes the __objects dictionary to the JSON file"""
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_dict, file)

    def reload(self):
        """
        imports the JSON file into the __objects dictionary if the JSON file
        exists
        """
        try:
            with open(self.__file_path, 'r') as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    class_name = key.split('.')[0]
                    if class_name == "BaseModel":
                        obj = BaseModel(**value)
                        self.__objects[key] = obj

        except FileNotFoundError:
            pass
