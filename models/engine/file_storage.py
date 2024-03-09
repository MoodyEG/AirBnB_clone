#!/usr/bin/python3
""" Storage handling file """
import os
import json


class FileStorage:
    """ Serializes instances to a JSON file
    and deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns all objects in the storage """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        data = {k: v.to_dict() for k,v in self.__objects.items()}
        with  open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if not os.path.exists(self.__file_path):
            return
        from models.base_model import BaseModel

        classes = {'BaseModel': BaseModel}
        with open(self.__file_path, 'r') as file:
            data = json.load(file)
        for key, value in data.items():
            obj = classes[value['__class__']](**value)
            self.__objects[key] = obj
