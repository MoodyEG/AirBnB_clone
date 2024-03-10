#!/usr/bin/python3
""" Test Module for State Module """
import unittest
from models.base_model import BaseModel
from models.state import State


class test_State(unittest.TestCase):
    """ Tesing State class """
    my_state = State()
    my_state.name = "ALX"

    def test1_attr(self):
        """ Checking for attributes """
        self.assertTrue("id" in self.my_state.__dict__)
        self.assertTrue("created_at" in self.my_state.__dict__)
        self.assertTrue("updated_at" in self.my_state.__dict__)
        self.assertTrue("name" in self.my_state.__dict__)

    def test2_attr(self):
        """ Checking for attributes """
        self.assertEqual(self.my_state.name, "ALX")

    def test3_attr(self):
        """ Checking for attributes """
        self.assertEqual(type(self.my_state.name), str)

    def test4_subclass(self):
        """ Checking if State is subclass to Base """
        self.assertTrue(issubclass(self.my_state.__class__, BaseModel), True)


if __name__ == '__main__':
    unittest.main()
