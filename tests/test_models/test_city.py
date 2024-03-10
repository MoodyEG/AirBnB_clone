#!/usr/bin/python3
""" Test Module for City Module """
import unittest
from models.base_model import BaseModel
from models.city import City


class test_City(unittest.TestCase):
    """ Tesing City class """
    my_city = City()
    my_city.name = "ALX"
    my_city.state_id = "sid"

    def test1_attr(self):
        """ Checking for attributes """
        self.assertTrue("id" in self.my_city.__dict__)
        self.assertTrue("created_at" in self.my_city.__dict__)
        self.assertTrue("updated_at" in self.my_city.__dict__)
        self.assertTrue("name" in self.my_city.__dict__)
        self.assertTrue("state_id" in self.my_city.__dict__)

    def test2_attr(self):
        """ Checking for attributes """
        self.assertEqual(self.my_city.name, "ALX")
        self.assertEqual(self.my_city.state_id, "sid")

    def test3_attr(self):
        """ Checking for attributes """
        self.assertEqual(type(self.my_city.name), str)
        self.assertEqual(type(self.my_city.state_id), str)

    def test4_subclass(self):
        """ Checking if City is subclass to Base """
        self.assertTrue(issubclass(self.my_city.__class__, BaseModel), True)


if __name__ == '__main__':
    unittest.main()
