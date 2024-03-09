#!/usr/bin/python3
""" Test Module for Base Module """
from models.base_model import BaseModel
import unittest
import json
from datetime import datetime



class test_BaseModel(unittest.TestCase):
    """ Tesing BaseModel class """
    model = BaseModel()

    def test_BaseModel(self):
        """ Test of BaseModel """

        self.model.name = "Hello"
        self.model.number = 24
        self.model.save()
        model_json = self.model.to_dict()
        self.assertEqual(self.model.name, model_json['name'])
        self.assertEqual(self.model.number, model_json['number'])
        self.assertEqual('BaseModel', model_json['__class__'])
        self.assertEqual(self.model.id, model_json['id'])
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.model.save()
        self.assertNotEqual(self.model.updated_at, self.model.created_at)

if __name__ == '__main__':
    unittest.main()
