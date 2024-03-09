#!/usr/bin/python3

""" Showing the Utilities/Amenity of the Class 
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
