#!/usr/bin/env python3
"""Module for base model"""
import unittest
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """Base model tests"""

    def test_creation(self):
        """Checks that an instance can be created with
        appropriate values"""
        my_model = BaseModel()
        self.assertIsNotNone(my_model)
        self.assertIsNotNone(my_model.id)

    def test_str(self):
        """checks the string representation of a class"""
        my_model = BaseModel()
        id = my_model.id
        strn = f'[BaseModel] ({id}) {my_model.__dict__}'
        self.assertEqual(strn, my_model.__str__())

    def test_todict(self):
        """checks the dictionary rep of a BaseModel
        instance"""
        my_model = BaseModel()
        model_dict = {'id': my_model.id}
        created_at = my_model.created_at.isoformat()
        updated_at = my_model.updated_at.isoformat()
        model_dict['created_at'] = created_at
        model_dict['updated_at'] = updated_at
        model_dict['__class__'] = 'BaseModel'
        self.assertEqual(model_dict, my_model.to_dict())


if __name__ == '__main__':
    unittest.main()
