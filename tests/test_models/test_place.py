#!/usr/bin/python3
""" Test Module for Place Module """
import unittest
from models.base_model import BaseModel
from models.place import Place


class test_Place(unittest.TestCase):
    """ Tesing place class """
    my_place = Place()
    my_place.name = "ALX"
    my_place.city_id = "city_id"
    my_place.user_id = "user_id"
    my_place.description = "description"
    my_place.number_rooms = 11
    my_place.number_bathrooms = 12
    my_place.max_guest = 13
    my_place.price_by_night = 14
    my_place.latitude = 15.5
    my_place.longitude = 16.6
    my_place.amenity_ids = ["ALX"]

    def test1_attr(self):
        """ Checking for attributes """
        self.assertTrue("id" in self.my_place.__dict__)
        self.assertTrue("created_at" in self.my_place.__dict__)
        self.assertTrue("updated_at" in self.my_place.__dict__)
        self.assertTrue("name" in self.my_place.__dict__)
        self.assertTrue("city_id" in self.my_place.__dict__)
        self.assertTrue("user_id" in self.my_place.__dict__)
        self.assertTrue("description" in self.my_place.__dict__)
        self.assertTrue("number_rooms" in self.my_place.__dict__)
        self.assertTrue("number_bathrooms" in self.my_place.__dict__)
        self.assertTrue("max_guest" in self.my_place.__dict__)
        self.assertTrue("price_by_night" in self.my_place.__dict__)
        self.assertTrue("latitude" in self.my_place.__dict__)
        self.assertTrue("longitude" in self.my_place.__dict__)
        self.assertTrue("amenity_ids" in self.my_place.__dict__)

    def test2_attr(self):
        """ Checking for attributes """
        self.assertEqual(self.my_place.name, "ALX")
        self.assertEqual(self.my_place.city_id, "city_id")
        self.assertEqual(self.my_place.description, "description")
        self.assertEqual(self.my_place.number_rooms, 11)
        self.assertEqual(self.my_place.number_bathrooms, 12)
        self.assertEqual(self.my_place.max_guest, 13)
        self.assertEqual(self.my_place.price_by_night, 14)
        self.assertEqual(self.my_place.latitude, 15.5)
        self.assertEqual(self.my_place.longitude, 16.6)
        self.assertEqual(self.my_place.amenity_ids, ["ALX"])

    def test3_attr(self):
        """ Checking for attributes """
        self.assertEqual(type(self.my_place.name), str)
        self.assertEqual(type(self.my_place.city_id), str)
        self.assertEqual(type(self.my_place.description), str)
        self.assertEqual(type(self.my_place.number_rooms), int)
        self.assertEqual(type(self.my_place.number_bathrooms), int)
        self.assertEqual(type(self.my_place.max_guest), int)
        self.assertEqual(type(self.my_place.price_by_night), int)
        self.assertEqual(type(self.my_place.latitude), float)
        self.assertEqual(type(self.my_place.longitude), float)
        self.assertEqual(type(self.my_place.amenity_ids), list)

    def test4_subclass(self):
        """ Checking if Place is subclass to Base """
        self.assertTrue(issubclass(self.my_place.__class__, BaseModel), True)


if __name__ == '__main__':
    unittest.main()
