#!/usr/bin/python3
""" Test Module for Amenity Module """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """ Tesing Amenity class """
    my_amenity = Amenity()
    my_amenity.name = "ALX"

    def test1_attr(self):
        """ Checking for attributes """
        self.assertTrue("id" in self.my_amenity.__dict__)
        self.assertTrue("created_at" in self.my_amenity.__dict__)
        self.assertTrue("updated_at" in self.my_amenity.__dict__)
        self.assertTrue("name" in self.my_amenity.__dict__)

    def test2_attr(self):
        """ Checking for attributes """
        self.assertEqual(self.my_amenity.name, "ALX")

    def test3_attr(self):
        """ Checking for attributes """
        self.assertEqual(type(self.my_amenity.name), str)

    def test4_subclass(self):
        """ Checking if Amenity is subclass to Base """
        self.assertTrue(issubclass(self.my_amenity.__class__, BaseModel), True)


if __name__ == '__main__':
    unittest.main()
