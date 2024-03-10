#!/usr/bin/python3
""" Test Module for User Module """
from models.user import User
from models.base_model import BaseModel
import unittest
from datetime import datetime


class test_User(unittest.TestCase):
    """ Tesing User class """
    my_user = User()
    my_user.first_name = "Betty"
    my_user.last_name = "Bar"
    my_user.email = "airbnb@mail.com"
    my_user.password = "root"

    def test1_attr(self):
        """ Checking for attributes """
        self.assertTrue("email" in self.my_user.__dict__)
        self.assertTrue("id" in self.my_user.__dict__)
        self.assertTrue("created_at" in self.my_user.__dict__)
        self.assertTrue("updated_at" in self.my_user.__dict__)
        self.assertTrue("password" in self.my_user.__dict__)
        self.assertTrue("first_name" in self.my_user.__dict__)
        self.assertTrue("last_name" in self.my_user.__dict__)
        self.assertEqual(self.my_user.first_name, "Betty")
        self.assertEqual(self.my_user.last_name, "Bar")
        self.assertEqual(self.my_user.email, "airbnb@mail.com")
        self.assertEqual(self.my_user.password, "root")
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.last_name), str)
        self.assertEqual(type(self.my_user.email), str)
        self.assertEqual(type(self.my_user.password), str)

    def test2_subclass(self):
        """ Checking if User is subclass to Base """
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel), True)


if __name__ == '__main__':
    unittest.main()
