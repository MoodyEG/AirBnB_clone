#!/usr/bin/python3
""" Test Module for Review Module """
import unittest
from models.base_model import BaseModel
from models.review import Review


class test_Review(unittest.TestCase):
    """ Tesing Review class """
    my_review = Review()
    my_review.place_id = "pid"
    my_review.user_id = "uid"
    my_review.text = "text"

    def test1_attr(self):
        """ Checking for attributes """
        self.assertTrue("id" in self.my_review.__dict__)
        self.assertTrue("created_at" in self.my_review.__dict__)
        self.assertTrue("updated_at" in self.my_review.__dict__)
        self.assertTrue("place_id" in self.my_review.__dict__)
        self.assertTrue("user_id" in self.my_review.__dict__)
        self.assertTrue("text" in self.my_review.__dict__)

    def test2_attr(self):
        """ Checking for attributes """
        self.assertEqual(self.my_review.user_id, "uid")
        self.assertEqual(self.my_review.place_id, "pid")
        self.assertEqual(self.my_review.text, "text")

    def test3_attr(self):
        """ Checking for attributes """
        self.assertEqual(type(self.my_review.user_id), str)
        self.assertEqual(type(self.my_review.text), str)
        self.assertEqual(type(self.my_review.place_id), str)

    def test4_subclass(self):
        """ Checking if Review is subclass to Base """
        self.assertTrue(issubclass(self.my_review.__class__, BaseModel), True)


if __name__ == '__main__':
    unittest.main()
