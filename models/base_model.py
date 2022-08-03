#!/usr/bin/env python3
"""This module defines the class BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """This class  defines all common attributes/methods
    for other classes"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation of an instance of
        BaseModel"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """saves this instance of the BaseModel"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary representation of an instance of
        BaseModel"""
        dict_rep = self.__dict__
        dict_rep['__class__'] = 'BaseModel'
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
