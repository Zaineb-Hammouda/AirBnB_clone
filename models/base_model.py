#!/usr/bin/python3

"""
This is the base model for which other classes inherit public
instance attributes and methods
"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """
    Base Model with all common methods and attributes

    Class_methods:
        __init__: Instantiation of attributes
        save: Updates the public instance attribute with the current time
        to_dict: Returns a dictionary with all keys of __dict__
        __str__: base class attributes in string format
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiation of attributes.

        args:
            *args: This is the variable length of the list of arguments
            **kwargs: This allows to pass any number of keyword arguments

        If kwargs != empty:
            * each key corresponds to an attribute name
            * each value in the kwargs dictionary is used as a value
            * Specifically, if the attribute name is 'created_at' or
                'updated_at', their values are converted to datetime objects
        Else:
            * id is generated using uuid.uuid4()
            * created_at attribute os set to the current datetime
            * updated_at is also set to the current datetime,
                matching created_at
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Representation of base class attributes in string format."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """updated_at is updated with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Dictionary is returned containing all keys of __dict__ of the instance.
        """
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        return dict_repr
