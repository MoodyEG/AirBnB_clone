#!/usr/bin/python3
"""Base Module"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """ Initialzing the class """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    timeformat = "%Y-%m-%dT%H:%M:%S.%f"
                    value = datetime.strptime(kwargs[key], timeformat)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """ Return a representation of the class """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary representation of the object """
        dic = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dic[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if value:
                    dic[key] = value
        dic['__class__'] = self.__class__.__name__
        return dic
