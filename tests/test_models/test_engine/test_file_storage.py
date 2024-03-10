#!/usr/bin/python3
""" Test for FileStorage """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class test_FileStorage(unittest.TestCase):
    """ Testing FileStorage class """
    model = BaseModel()

    def test1_class(self):
        """ Check instance """
        self.assertIsInstance(storage, FileStorage)

    def test2_save(self):
        """ Check for save function """
        self.model.name = "Hello again"
        self.model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)
        data_dic = self.model.to_dict()
        data_storage = storage.all()
        key = data_dic["__class__"] + "." + data_dic["id"]
        c1 = data_dic["created_at"]
        u1 = data_dic["updated_at"]
        self.assertEqual(key in data_storage, True)
        self.assertEqual(data_dic["name"], "Hello again")
        self.model.name = "Hello Hello"
        self.model.save()
        data_dic = self.model.to_dict()
        data_storage = storage.all()
        c2 = data_dic["created_at"]
        u2 = data_dic["updated_at"]
        self.assertEqual(key in data_storage, True)
        self.assertEqual(data_dic["name"], "Hello Hello")
        self.assertEqual(c1, c2)
        self.assertNotEqual(u1, u2)

    def test3_reload(self):
        """ checking reload function """
        self.model.save()
        data_storage = storage.all()
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(data_storage[key].to_dict(), value.to_dict())

    def test4_files(self):
        """ Checking the file generated, had help """
        f1 = self.model.to_dict()
        key = f1['__class__'] + "." + f1['id']
        storage.save()
        with open("file.json", 'r') as file:
            loaded = json.load(file)
        f2 = loaded[key]
        for data in f2:
            self.assertEqual(f1[data], f2[data])

    def test5_attr(self):
        """ Checking Attributes """
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def test6_save(self):
        """verify if JSON exists"""
        self.model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
